import json
import time
import os
import random


# It's will be keep old value
global_random = random.random()

def cold_start_basic(event, context):
    print("****************************************")
    local_random = random.random()
    print(local_random)
    print(global_random)

def simple_types(event, context):
    print(event)
    return event

def list_types(event: list, context) -> list:
    print(event)
    student_scores = {"Join":100, "Hiep": 99, "Nguyen": 90}
    return [student_scores.get(e, None) for e in event]

def dict_types(event, context):
    print(event)

def context_object(event, context):
    print("****************************************")
    print("Lambda function Name:", context.function_name)
    print("Lambda function Version:", context.function_version)
    print("Lambda function ARN:", context.invoked_function_arn)
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    # and Test Timeout
    # time.sleep(0)
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())
    # Get environment variables
    print(os.getenv("ROOT_URL", None))
    print("****************************************")
