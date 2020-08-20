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
	message_summary = build_message_summary(comprehend_response)
	
	
def build_message_summary(comprehend_response):
	message_summary = ''
	
	return message_summary

