import os
import sys
import traceback
import json
import glob
import logging
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)


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
    path = os.environ['LAMBDA_TASK_ROOT'] + '/LoadTestData/test_*.json'
    test_files = glob.glob(path)
    bucket = os.environ['TEST_DATA_TARGET_S3_BUCKET']
    prefix = os.environ['TEST_DATA_TARGET_S3_PREFIX']
    logger.info(f'using the following files as test data: {test_files}')
    num_messages = 16732
    start_date = datetime.datetime.strptime('2020-03-01', '%Y-%m-%d')
    end_date = datetime.datetime.now()
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
    # load test files
    test_messages = []
    for test_file in test_files:
        with open(test_file) as f:
            test_messages.append(json.load(f))
    
    
    
