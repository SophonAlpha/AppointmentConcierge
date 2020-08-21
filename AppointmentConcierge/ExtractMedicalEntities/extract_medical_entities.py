import os
import sys
import logging
import traceback
import json
import boto3
import datetime
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class DBTableNameNotConfigured(Exception):
    """
    Custom error class: thrown when the lambda environment
    variable 'DB_TABLE_NAME' is not configured.
    """

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
		extract_medical_entities(event, context)
	except Exception:
		exception_type, exception_value, exception_traceback = sys.exc_info()
		traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
		err_msg = json.dumps({
			"errorType": exception_type.__name__,
			"errorMessage": str(exception_value),
			"stackTrace": traceback_string
		})
		logger.error(err_msg)

def extract_medical_entities(event, context):
	# get parameters for comprehend job
	bucket_name = event['Records'][0]['s3']['bucket']['name']
	key = event['Records'][0]['s3']['object']['key']
	file_url = f's3://{bucket_name}/{key}'
	s3 = boto3.client('s3')
	s3_obj = s3.get_object(Bucket = bucket_name, Key = key)
	response = json.loads(s3_obj['Body'].read().decode('utf-8'))
	text = response['results']['transcripts'][0]['transcript']
	comprehend = boto3.client('comprehendmedical', region_name = 'eu-west-1')
	
	# run comprehend job
	logger.info('detecting medical entities ...')
	comprehend_response = comprehend.detect_entities_v2(Text = text)
	logger.info(
		f'the following response has been received form the '
		f'Comprehend Medical service:{json.dumps(comprehend_response)}')

	# save results to database
	db_table_name = os.environ.get('DB_TABLE_NAME', False)
	if not db_table_name:
		raise DBTableNameNotConfigured(
			'Environment variable \'DB_TABLE_NAME\' is not defined.')
	logger.info('saving data to database ...')
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table(db_table_name)
	ddb_data = json.loads(json.dumps(comprehend_response), parse_float=Decimal)
	ddb_data['time'] = f'{datetime.datetime.now()}'
	table_response = table.put_item(Item = ddb_data)
	logger.info(
		f'the following response has been received form the '
		f'database service:{json.dumps(table_response)}')
	
	# build message summary in html
	msg_html_doc = build_message_summary(text,
										 comprehend_response,
										 s3_obj['LastModified'])
	# save HTML document to S3 bucket
	
	
	
def build_message_summary(text, comprehend_response, msg_time):
	"""
	Put message information into HTML formatted document.
	"""
	phi_map = {
		'phi_type': ['NAME', 'AGE', 'ADDRESS', 'PROFESSION', 'EMAIL',
				     'IDENTIFIER', 'CONTACT_POINT'],
		'summary_text': ['Name', 'Age', 'Address', 'Profession', 'Email',
				         'Identifier', 'Contact']
	}
	medical_categories = ['MEDICAL_CONDITION', 'ANATOMY', 'MEDICATION',
						  'TEST_TREATMENT_PROCEDURE']
	msg_data = {}
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
	# build HTML document
	msg_html_doc = '<html><head><style>body {font-family: Arial, ' \
		'serif;font-size: 14px;}</style><title></title></head><body>'
	msg_html_doc += '<H1 style="color:#b30000" align="center">' \
		'Voice Message Transcript</H1><hr>'
	msg_html_doc += f'<p><b>Message Received : </b>' \
					f'{msg_time.strftime("%B %d, %Y %H:%M:%S")}</p>'
	msg_html_doc += f'<p><b>Transcript : </b>{text}</p>'
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

