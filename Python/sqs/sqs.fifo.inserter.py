#!/usr/bin/python3

import boto3
import random

sqs = boto3.client('sqs')
#response = sqs.list_queues()
#print(response['QueueUrls'])

# Fifo queues have different requirements for keys inside sqs.send_message than Standard Q's.
queue_url = 'https://queue.amazonaws.com/308303745136/SL-test-FQ.fifo'

# Send message to SQS queue
count = 0
while count < 10:
    count_str = str(count)
    response = sqs.send_message(
        MessageGroupId=count_str,
        MessageDeduplicationId='b910a47{0}{1}'.format(count, random.randint(1,1000000)),
        QueueUrl=queue_url,
        MessageBody=(
            'Information'
        )
    )

    count += 1
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        print(response)
