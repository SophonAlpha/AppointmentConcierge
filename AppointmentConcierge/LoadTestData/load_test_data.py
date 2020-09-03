import os
import sys
import traceback
import json
import glob
import logging
import datetime
import uuid
import random
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize boto3 client at global scope for connection reuse
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
	Entry point for the lambda function. Will be triggered as a custom resource by CDK.
	Loads test data to populate for the QuickSight dashboard.
	
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
    # set up parameters
    path = os.environ['LAMBDA_TASK_ROOT'] + '/test_*.json'
    test_files = glob.glob(path)
    logger.info(f'using the following files as test data: {test_files}')
    bucket = os.environ['TEST_DATA_TARGET_S3_BUCKET']
    prefix = os.environ['TEST_DATA_TARGET_S3_PREFIX']
    logger.info(f'configured target S3 bucket and prefix: {bucket + "/" + prefix}')
    num_messages = int(os.environ['NUM_MESSAGES'])
    logger.info(f'number of test messages to be created: {num_messages}')
    start_date = datetime.datetime.strptime(
        os.environ['START_DATE'], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(
        os.environ['END_DATE'], '%Y-%m-%d')
    logger.info(f'configured start date: {start_date.strftime("%Y-%m-%d")}')
    logger.info(f'configured end date: {end_date.strftime("%Y-%m-%d")}')
    weekday_weights = {0: 4, # Monday
                       1: 2, # Tuesday
                       2: 2, # Wednesday
                       3: 1, # Thursday
                       4: 2, # Friday
                       5: 1, # Saturday
                       6: 5} # Sunday
    # paramters for random.choices()
    start_weekday = start_date.weekday()
    num_days = (end_date - start_date).days
    weights = [weekday_weights[day % 7]
               for day in range(start_weekday, start_weekday + num_days)]
    dates = [start_date + datetime.timedelta(days=day)
             for day in range((end_date - start_date).days)]
    # load test messages
    test_messages = []
    for test_file in test_files:
        with open(test_file) as f:
            test_messages.append(json.load(f))
    # write test messages to S3 bucket
    nth_msg = 100
    for idx, _ in enumerate(range(num_messages)):
        message_time = random.choices(dates, weights=weights)[0] + \
                       datetime.timedelta(seconds=random.randrange(24 * 60 * 60))
        new_message = test_messages[random.randrange(len(test_messages))]
        new_message['messageTime'] = message_time.strftime('%Y-%m-%d %H:%M:%S')
        new_message['messageId'] = str(uuid.uuid4())
        save_dict_to_s3(new_message, bucket, prefix, new_message['messageId'] + '.json')
        if (idx + 1) % nth_msg == 0:
            logger.info(f'{idx + 1} test messages written to {bucket + "/" + prefix}')
    logger.info(f'{num_messages} test messages written to {bucket + "/" + prefix}')


def save_dict_to_s3(dict_obj, bucket_name, prefix, file_name):
	"""
	Save dictionary object as JSON document in S3.
	"""
	s3_response = s3.put_object(
		Body=bytes(json.dumps(dict_obj, default=str), 'utf-8'),
		Bucket=bucket_name,
		Key=f'{prefix}{file_name}')
	if not s3_response['ResponseMetadata']['HTTPStatusCode'] == 200:
		logger.error(f'Error: S3 service returned HTTP status code ' \
                     f'{s3_response["ResponseMetadata"]["HTTPStatusCode"]}.')
