#!/usr/bin/python3

import boto3
import sys

sqs = boto3.client('sqs')

# Fifo queues have different requirements for keys inside sqs.send_message than Standard Q's. 
queue_url = 'https://queue.amazonaws.com/308303745136/sl_queue.fifo'

'''while True:
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
'''

counter = 0
queue = sqs.

# Process messages by printing out body from test Amazon SQS Queue
for message in queue.receive_messages(QueueUrl=queue_url):
    counter += 1
    message.delete()


messages = queue.receive_messages()
for message in messages:
   print('Body: {0}'.format(message.body))
   message.delete()

print(counter)
