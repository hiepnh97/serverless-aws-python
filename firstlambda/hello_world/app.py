import json


def first_lambda(event, context):
    ''''''
    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "hello world" + event,
    #         # "location": ip.text.replace("\n", "")
    #     }),
    # }
    return "Hello " + event
