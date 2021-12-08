

def bill_management(event, context):
    message = event['Records'][0]['Sns']['Message']
    print(message)
