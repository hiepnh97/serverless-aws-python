import json
import boto3
import os

s3 = boto3.client('s3')
sns_client = boto3.client('sns')


def push_message_to_SNS(event, context):
    topic = os.environ.get('PATIENT_CHECKOUT_TOPIC')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    print(f'******** bucket_name: {bucket_name} -- file_key: {file_key}')
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = obj['Body'].read().decode('utf-8')
    checkout_events = json.loads(file_content)
    for event in checkout_events:
        print(event)
        sns_client.publish(
            TopicArn=topic,
            Message=json.dumps({'default': json.dumps(event)}),
            MessageStructure='json'
        )
