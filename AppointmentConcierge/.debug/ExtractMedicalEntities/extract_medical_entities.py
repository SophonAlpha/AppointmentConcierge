import os
import sys
import logging
import traceback
import json
import boto3
import datetime
from decimal import Decimal

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize boto3 client at global scope for connection reuse
s3 = boto3.client('s3')
comprehend = boto3.client('comprehendmedical', region_name='eu-west-1')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
	"""
	Entry point for the lambda function. Will be triggered by an transcription file
	uploaded to the S3 bucket.
	
	This function primary pupose is to setup logging and ansure we get any
	exception information into CloudWatch.
	"""
	try:
		logger.info(f'Received the following event data: \
			{json.dumps(event, indent=4)}')
		# let's start the actual work
		process_event(event, context)
	except Exception:
		exception_type, exception_value, exception_traceback = sys.exc_info()
		traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
		err_msg = json.dumps({
			"errorType": exception_type.__name__,
			"errorMessage": str(exception_value),
			"stackTrace": traceback_string
		})
		logger.error(err_msg)


def process_event(event, context):
	"""
	Process the received event.
	"""
	comprehend_response = extract_medical_entities(event)
	file_name = comprehend_response[
		'messageTranscriptFileUrl'].split('/')[-1].split('.')[0] + '.json'
	save_dict_to_s3(comprehend_response,
	                os.environ['MSG_DOC_S3_BUCKET'],
	                os.environ['COMPREHEND_RESULTS_S3_PREFIX'],
	                file_name)
	save_to_db(comprehend_response)
	msg_data = extract_msg_details(comprehend_response)
	msg_html_doc = build_message_doc(msg_data)
	save_to_s3(msg_html_doc, comprehend_response['messageTranscriptFileUrl'])


def extract_medical_entities(event):
	"""
	Extract medical entities using Amazon Comprehend Medical.
	"""
	# set up parameters for comprehend job
	bucket_name = event['Records'][0]['s3']['bucket']['name']
	key = event['Records'][0]['s3']['object']['key']
	file_url = f's3://{bucket_name}/{key}'
	s3_obj = s3.get_object(Bucket=bucket_name, Key=key)
	response = json.loads(s3_obj['Body'].read().decode('utf-8'))
	text = response['results']['transcripts'][0]['transcript']
	# run comprehend job
	logger.info('Start: detecting medical entities.')
	comprehend_response = comprehend.detect_entities_v2(Text=text)
	if comprehend_response['ResponseMetadata']['HTTPStatusCode'] == 200:
		comprehend_response['messageTime'] = (s3_obj['LastModified'] + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S')
		comprehend_response['messageId'] = file_url.split('/')[-1].split('.')[0]
		comprehend_response['messageTranscriptText'] = text
		comprehend_response['messageTranscriptFileUrl'] = file_url
		logger.info('Success: detecting medical entities completed.')
	else:
		logger.error(f'Error: Comprehend service returned HTTP status code ' \
                     f'{comprehend_response["ResponseMetadata"]["HTTPStatusCode"]}.')
	return comprehend_response


def save_dict_to_s3(dict_obj, bucket_name, prefix, file_name):
	"""
	Save dictionary object as JSON document in S3.
	"""
	logger.info('Start: saving the Comprehend Medical results to S3.')
	s3_response = s3.put_object(
		Body=bytes(json.dumps(dict_obj, default=str), 'utf-8'),
		Bucket=bucket_name,
		Key=f'{prefix}{file_name}')
	if s3_response['ResponseMetadata']['HTTPStatusCode'] == 200:
		logger.info('Success: Comprehend Medical results saved to S3.')
	else:
		logger.error(f'Error: S3 service returned HTTP status code ' \
                     f'{s3_response["ResponseMetadata"]["HTTPStatusCode"]}.')
	

def save_to_db(comprehend_response):
	"""
	Save information received from Amazon Comprehend Medical to DynamoDB database.
	"""
	# save results to database
	db_table_name = os.environ['DB_TABLE_NAME']
	logger.info('Start: saving data to database.')
	table = dynamodb.Table(db_table_name)
	ddb_data = json.loads(
		json.dumps(comprehend_response, default=str),
		parse_float=Decimal)
	table_response = table.put_item(Item=ddb_data)
	if table_response['ResponseMetadata']['HTTPStatusCode'] == 200:
		logger.info('Success: data written to database.')
	else:
		logger.error(f'Error: database service returned HTTP status code ' \
                     f'{table_response["ResponseMetadata"]["HTTPStatusCode"]}.')


def extract_msg_details(comprehend_response):
	"""
	Extract information from comprehend result and store in dictionary.
	"""
	phi_map = {
		'phi_type': ['NAME', 'AGE', 'ADDRESS', 'PROFESSION', 'EMAIL',
				     'IDENTIFIER', 'CONTACT_POINT'],
		'summary_text': ['Name', 'Age', 'Address', 'Profession', 'Email',
				         'Identifier', 'Contact']
	}
	medical_categories = ['MEDICAL_CONDITION', 'ANATOMY', 'MEDICATION',
						  'TEST_TREATMENT_PROCEDURE']
	msg_data = {
		'message time': comprehend_response["messageTime"],
		'message transcript text': comprehend_response["messageTranscriptText"],
	}
	for entity in comprehend_response['Entities']:
		# set up sections
		if entity['Category'] == 'PROTECTED_HEALTH_INFORMATION' and \
			not msg_data.get('PHI', False):
				# set up PHI section
				msg_data['PHI'] = {}
		if entity['Category'] in medical_categories and \
			not msg_data.get('details', False):
				# set up PHI section
				msg_data['details'] = {}
		# extract PROTECTED_HEALTH_INFORMATION entities
		if entity['Type'] in phi_map['phi_type']:
			idx = phi_map['phi_type'].index(entity['Type'])
			msg_data['PHI'][phi_map['summary_text'][idx]] = entity['Text']
		# extract MEDICAL_CONDITION entities
		if entity['Category'] == 'MEDICAL_CONDITION':
			if msg_data['details'].get('Symptoms', False):
				msg_data['details']['Symptoms'].append(entity['Text'])
			else:
				msg_data['details']['Symptoms'] = [entity['Text']]
		# extract ANATOMY entities
		if entity['Category'] == 'ANATOMY':
			if msg_data['details'].get('Anatomy', False):
				msg_data['details']['Anatomy'].append(entity['Text'])
			else:
				msg_data['details']['Anatomy'] = [entity['Text']]
		# extract MEDICATION entities
		if entity['Category'] == 'MEDICATION':
			if msg_data['details'].get('Medication', False):
				msg_data['details']['Medication'].append(entity['Text'])
			else:
				msg_data['details']['Medication'] = [entity['Text']]
		# extract TEST_TREATMENT_PROCEDURE entities
		if entity['Category'] == 'TEST_TREATMENT_PROCEDURE':
			if msg_data['details'].get('Treatments, Tests, Procedures', False):
				msg_data['details']['Treatments, Tests, Procedures'].append(entity['Text'])
			else:
				msg_data['details']['Treatments, Tests, Procedures'] = [entity['Text']]
	return msg_data


def build_message_doc(msg_data):
	"""
	Put message information into HTML formatted document.
	"""
	# build HTML document
	msg_html_doc = '<html><head><style>body {font-family: Arial, ' \
		'serif;font-size: 14px;}</style><title></title></head><body>'
	msg_html_doc += '<H1 style="color:#b30000" align="center">' \
		'Voice Message Transcript</H1><hr>'
	msg_html_doc += f'<p><b>Message Received : </b>' \
					f'{msg_data["message time"]}</p>'
	msg_html_doc += f'<p><b>Transcript : </b>{msg_data["message transcript text"]}</p>'
	# add section with PHI
	if msg_data.get('PHI', False):
		msg_html_doc += '<hr>'
		for key in msg_data['PHI'].keys():
			msg_html_doc += f'<p><b>{key} : </b>{msg_data["PHI"][key]}</p>'
	# add section with medical details
	if msg_data.get('details', False):
		msg_html_doc += '<hr>'
		for key in msg_data['details'].keys():
			msg_html_doc += f'<p><b>{key} : </b>{", ".join(msg_data["details"][key])}</p>'
	# end of HTML document
	msg_html_doc += '</body></html>'
	return msg_html_doc


def save_to_s3(msg_html_doc, file_url):
	"""
	Save the message HTML document to S3.
	"""
	logger.info('Start: saving the message HTML document to S3.')
	bucket_name = os.environ['MSG_DOC_S3_BUCKET']
	prefix = os.environ['MSG_DOC_S3_PREFIX']
	file_name = file_url.split('/')[-1].split('.')[0] + '.html'
	s3_response = s3.put_object(
		Body=bytes(msg_html_doc, 'utf-8'),
		Bucket=bucket_name,
		Key=f'{prefix}{file_name}')
	if s3_response['ResponseMetadata']['HTTPStatusCode'] == 200:
		logger.info('Success: message HTML document written to S3.')
	else:
		logger.error(f'Error: database service returned HTTP status code ' \
                     f'{s3_response["ResponseMetadata"]["HTTPStatusCode"]}.')
