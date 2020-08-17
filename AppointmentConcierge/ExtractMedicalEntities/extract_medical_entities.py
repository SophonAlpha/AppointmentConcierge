import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
	logger.info('I\'m the extract_medical_entities lambda function.')
	if os.environ.get('AWS_SAM_LOCAL', False) and os.environ.get('AWS_SAM_LOCAL') == 'true':
		logger.info('running locally')
	else:
		logger.info('running remotely')
	logger.info(os.environ)
	return ''