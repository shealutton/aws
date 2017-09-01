#!/usr/bin/python3

import boto3
import sys

sqs = boto3.client('sqs')
#response = sqs.list_queues()
#print(response['QueueUrls'])
#sys.exit(0)

# Fifo queues have different requirements for keys inside sqs.send_message than Standard Q's. 
#queue_url = 'https://queue.amazonaws.com/308303745136/SL-test-FQ.fifo'
queue_url = 'https://queue.amazonaws.com/308303745136/SL-test-SQ'

while True:
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    try:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
    except KeyError:
        print('No messages to receive')
        sys.exit(1)

    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print('Received and deleted message: %s' % message)

