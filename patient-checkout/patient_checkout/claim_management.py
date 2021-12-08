import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def claim_management(event, context):
    for record in event['Records']:
        logger.info(f'******** {record["body"]} ******')
