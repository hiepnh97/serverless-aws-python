import os
import simplejson as json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')
table = dynamodb.Table(table_name)


def get_order(event, context):
    '''Function handler for get data orders from DynamoDB By Order Id'''
    print(table_name)
    order_id = int(event['pathParameters']['id'])
    print('=========order_id========', order_id)
    response = table.query(KeyConditionExpression=Key('id').eq(order_id))
    print(response)
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }

'''simplejson for handler case
{'Items': [{'id': Decimal('1'), 'name': 'order01'}], 'Count': 1, 'ScannedCount': 1, 'ResponseMetadata': {'RequestId': 'GA8AP9HHO8S7S56B209982808JVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Tue, 07 Dec 2021 08:15:06 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '78', 'connection': 'keep-alive', 'x-amzn-requestid': 'GA8AP9HHO8S7S56B209982808JVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '1519417617'}, 'RetryAttempts': 0}}
[ERROR] TypeError: Object of type Decimal is not JSON serializable
'''
