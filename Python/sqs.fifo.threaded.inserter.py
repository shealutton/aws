import boto3
import random
import threading
import time


###
# THIS APP IS NOT THREAD SAFE! THE BOTO SQS WILL CORE OUT WITH THREAD ISSUES
###

def inserter(name):
    sqs = boto3.client('sqs')
    #response = sqs.list_queues()
    #print(response['QueueUrls'])

    # Fifo queues have different requirements for keys inside sqs.send_message than Standard Q's.
    queue_url = 'https://queue.amazonaws.com/308303745136/SL-test-FQ.fifo'

    # Send message to SQS queue
    count = 0
    while count < 3:
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
        #if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        print(name, response)


t1 = threading.Thread(target = inserter, args = ('A'))
t2 = threading.Thread(target = inserter, args = ('B'))
t3 = threading.Thread(target = inserter, args = ('C'))
t4 = threading.Thread(target = inserter, args = ('D'))
t5 = threading.Thread(target = inserter, args = ('E'))
t6 = threading.Thread(target = inserter, args = ('F'))
t7 = threading.Thread(target = inserter, args = ('G'))

t1.start()
t2.start()
t3.start()
#t4.start()
#t5.start()
#t6.start()
#t7.start()
