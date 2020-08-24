import os
import sys
import logging
import traceback
import json
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize boto3 client at global scope for connection reuse
transcribe = boto3.client('transcribe')


def lambda_handler(event, context):
	"""
	Entry point for the lambda function. Will be triggered by an audio file
	uploaded to the S3 bucket.
	
	This function primary pupose is to setup logging and ansure we get any
	exception information into CloudWatch.
	"""
	try:
		logger.info(f'Received the following event data: \
			{json.dumps(event, indent=4)}')
		# let's start the actual work
		initiate_transciption_job(event, context)
	except Exception:
		exception_type, exception_value, exception_traceback = sys.exc_info()
		traceback_string = traceback.format_exception(
			exception_type, exception_value, exception_traceback)
		err_msg = json.dumps({
			"errorType": exception_type.__name__,
			"errorMessage": str(exception_value),
			"stackTrace": traceback_string
		})
		logger.error(err_msg)

def initiate_transciption_job(event, context):
	"""
	Setup and start the Transcribe job.
	"""
	output_bucket_name = os.environ['OUTPUT_BUCKET']
	file = event['Records'][0]
	bucket_name = file['s3']['bucket']['name']
	key = file['s3']['object']['key']
	file_name = key.split('/')[-1].split('.')[0]
	job_name = context.aws_request_id + '-' + file_name
	file_url = f's3://{bucket_name}/{key}'
	lang = 'en-US'
	job_json = json.dumps({
		'MedicalTranscriptionJobName': job_name,
		'Media': file_url,
		'LanguageCode': lang,
		'OutputBucketName': output_bucket_name,
		'Specialty': 'PRIMARYCARE',
    	'Type': 'CONVERSATION',
	})
	logger.info('Start: starting transcription job.')
	response = transcribe.start_medical_transcription_job(
		MedicalTranscriptionJobName = job_name,
		Media = {'MediaFileUri': file_url},
		LanguageCode = lang,
		OutputBucketName = output_bucket_name,
		Specialty = 'PRIMARYCARE',
    	Type = 'CONVERSATION',)
	if response['ResponseMetadata']['HTTPStatusCode'] == 200:
		logger.info('Success: transcription job started.')
		# covert datetime objects to string
		response['MedicalTranscriptionJob']['StartTime'] = f'{response["MedicalTranscriptionJob"]["StartTime"]}'
		response['MedicalTranscriptionJob']['CreationTime'] = f'{response["MedicalTranscriptionJob"]["CreationTime"]}'
		response['MedicalTranscriptionJob']['CompletionTime'] = f'{response["MedicalTranscriptionJob"]["CompletionTime"]}'
	else:
		logger.error(f'Error: Transcribe service returned HTTP status code ' \
                     f'{response["ResponseMetadata"]["HTTPStatusCode"]}.')
