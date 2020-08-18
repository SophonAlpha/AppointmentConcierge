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
	try:
		logger.info(f'Received the following event data: \
			{json.dumps(event, indent=4)}')
		initiate_transciption_job(event, context)
	except Exception:
		exception_type, exception_value, exception_traceback = sys.exc_info()
		traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
		err_msg = json.dumps({
			"errorType": exception_type.__name__,
			"errorMessage": str(exception_value),
			"stackTrace": traceback_string
		})
		logger.error(err_msg)

def initiate_transciption_job(event, context):
	output_bucket_name = os.environ.get('OUTPUT_BUCKET', False)
	if not output_bucket_name:
		raise OutputBucketNotConfigured(
			'Environment variable \'OUTPUT_BUCKET\' is not defined.')
	transcribe = boto3.client('transcribe')
	file = event['Records'][0]
	bucket_name = file['s3']['bucket']['name']
	key = file['s3']['object']['key']
	file_name = key.split('/')[-1].split('.')[0]
	job_name = context.aws_request_id + '-' + file_name
	file_url = f's3://{bucket_name}/{key}'
	lang = 'en-GB'
	job_json = json.dumps({
		'TranscriptionJobName': job_name,
		'Media': file_url,
		'LanguageCode': lang,
		'OutputBucketName': output_bucket_name,
	})
	logger.info(
		f'starting transcription job with the following parameters:{job_json}'
		)
	transcribe.start_transcription_job(
		TranscriptionJobName = job_name,
		Media = {'MediaFileUri': file_url},
		LanguageCode = lang,
		OutputBucketName = output_bucket_name)
