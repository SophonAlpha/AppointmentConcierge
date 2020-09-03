import os
import sys
import traceback
import json
import glob
import logging

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
    path = os.environ['LAMBDA_TASK_ROOT'] + '/LoadTestData/test_*.json'
    test_files = glob.glob(path)
    logger.info(f'using the following files as test data: {test_files}')
