import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')
table = dynamodb.Table(table_name)

def create_order(event, context):
    '''Function handler for creating a new order into DynamoDB'''
    print(table_name)
    order = json.loads(event['body'])
    print(order)
    response = table.put_item(TableName=table_name, Item=order)
    print(response)
    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'Message': 'Order created successfully!'})
    }
