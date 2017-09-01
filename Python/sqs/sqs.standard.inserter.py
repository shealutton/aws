#!/usr/bin/python3

import boto3

sqs = boto3.client('sqs')
#response = sqs.list_queues()
#print(response['QueueUrls'])

# Fifo queues have different requirements for keys inside sqs.send_message than Standard Q's. 
#queue_url = 'https://queue.amazonaws.com/308303745136/SL-test-FQ.fifo'
queue_url = 'https://queue.amazonaws.com/308303745136/SL-test-SQ'

# Send message to SQS queue
count = 0
while count < 1000:
    count_str = str(count)
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageAttributes={
            'Number': {
                'DataType': 'Number',
                'StringValue': count_str
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': count_str
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )
    count += 1
    print(response['MessageId'])

