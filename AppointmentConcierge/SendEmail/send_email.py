import os
import boto3
import json
import logging
import traceback
import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize boto3 client at global scope for connection reuse
ssm = boto3.client('ssm')
s3 = boto3.client('s3')


def lambda_handler(event, context):
	"""
	Entry point for the lambda function. Will be triggered by an message 
	document html file uploaded to the S3 bucket.
	
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
    config = load_config(os.environ['SSM_PS_APPCONFIG_PATH'])
    msg_doc = load_msg_doc(event)
    

def load_config(app_config_path):
    """
    Load configuration stored in SSM Parameter Store
    
    :param app_config_path: Path to configuration in SSM Parameter Store
    :return: dictionary holding configuration
    """
    logger.info('Start: retrieving configuration from Systems Manager Parameter Store.')
    config = {}
    param_details = ssm.get_parameters_by_path(
        Path=app_config_path,
        Recursive=True,
        WithDecryption=True)
    for param in param_details.get('Parameters'):
        param_path_array = param.get('Name').split("/")
        section_name = param_path_array[-1]
        config_values = json.loads(param['Value'])
        config = {section_name: config_values}
    logger.info('Success: configuration from Systems Manager Parameter Store retrieved.')
    return config


def load_msg_doc(event):
    """
    Reading the message HTML document from S3.ArithmeticError
    
    :param event: Lambda trigger event message 
    :return: message HTML document
    """
    logger.info(f'Start: reading message document from S3.')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    file_url = f's3://{bucket_name}/{key}'
    s3_obj = s3.get_object(Bucket=bucket_name, Key=key)
    if s3_obj['ResponseMetadata']['HTTPStatusCode'] == 200:
        msg_doc = s3_obj['Body'].read().decode('utf-8')
        logger.info('Success: reading message document from S3.')
    else:
        logger.error(f'Error: reading message document from S3 failed with ' \
                     f'HTTP status code {s3_obj["ResponseMetadata"]["HTTPStatusCode"]}.')
    return msg_doc