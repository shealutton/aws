#!/usr/bin/python3

import boto3
import random
import multiprocessing
import time




def sleeper (n, name):
    print('Hi, I am Process {}. Sleeping for 3 seconds.'.format(name))
    time.sleep(3)
    print('{} is now awake'.format(name))


def inserter(a, name):
    sqs = boto3.client('sqs')
    #response = sqs.list_queues()
    #print(response['QueueUrls'])

    # Fifo queues have different requirements for keys inside sqs.send_message than Standard Q's.
    queue_url = 'https://queue.amazonaws.com/308303745136/SL-test-FQ.fifo'

    # Send message to SQS queue
    count = 0
    while count < 1000:
        count_str = str(count)
        response = sqs.send_message(
            MessageGroupId=count_str,
            MessageDeduplicationId='{0}{1}{2}'.format(name, count, random.randint(1,1000000)),
            QueueUrl=queue_url,
            MessageBody=(
                'Information'
            )
        )

        count += 1
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(name, response)


if __name__ == '__main__':
    jobs = []
    for i in range(10):
        p = multiprocessing.Process(target=inserter, args=(i, i))
        jobs.append(p)
        p.start()
