import logging


logger = logging.getLogger('patient_checkout')
logger.setLevel(logging.INFO)


def bill_management(event, context):
    message = event['Records'][0]['Sns']['Message']
    logger.info(f'******* Message: {message}')
