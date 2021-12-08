import logging


logger = logging.getLogger('patient_checkout')
logger.setLevel(logging.INFO)


def error_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    logger.info(f'******* Error Handler - Message: {message}')
