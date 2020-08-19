import os
import sys
import logging
import traceback
import json
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class OutputBucketNotConfigured(Exception):
    """
    Custom error class: thrown when the lambda environment
    variable 'OUTPUT_BUCKET' is not defined.
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
	bucket_name = event['Records'][0]['s3']['bucket']['name']
	key = event['Records'][0]['s3']['object']['key']
	file_url = f's3://{bucket_name}/{key}'
	s3 = boto3.client('s3')
	s3_obj = s3.get_object(Bucket = bucket_name, Key = key)
	response = json.loads(s3_obj['Body'].read().decode('utf-8'))
	text = response['results']['transcripts'][0]['transcript']
	comprehend = boto3.client('comprehendmedical', region_name = 'eu-west-1')
	logger.info('detecting medical entities ...')
	response = comprehend.detect_entities_v2(Text = text)
	logger.info(
		f'the following response has been received form the '
		f'Comprehend Medical service:{json.dumps(response)}')
