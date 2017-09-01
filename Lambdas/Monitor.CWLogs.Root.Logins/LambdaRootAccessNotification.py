from __future__ import print_function

import json
import urllib
import boto3
import re

s3 = boto3.client('s3')


def doNotify(message):
    emailSubject = 'Root account login alert - please review'
    snsARN = 'arn:aws:sns:us-east-1:965097209055:shea-test'
    client = boto3.client('sns')
    response = client.publish(Subject=emailSubject,TargetArn=snsARN,Message=message)


def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        # Get the whole body of the file for parsing/regex
        contents = response["Body"].read()
        contents = json.loads(contents)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

    try:
        ### SET THIS REGEX EXPRESSION TO LOOK FOR YOUR ROOT ACCOUNT USER
        regex = r"arn:aws:iam:\w?:(\d+):root"
        root_login_found = False
        root_accounts = set()
    
        for line in contents['Records']:
            line_string = str(line)
            match = re.search(regex, line_string)
            if match:
                root_login_found = True
                print('Root login found for account:', match.group(0), match.group(1))
                root_accounts.add(match.group(1))
    except Exception as e:
        print(e)
        print('Error performing regex on {} from bucket {}. Make sure the file is CloudWatch .json format.'.format(key, bucket))
        raise e
    
    try:
        if root_login_found:
            message_text = 'Root user accounts should not be used except in emergencies. A root login was detected in the following account(s)'
            for account in root_accounts:
                message_text = '{0}, {1}'.format(message_text, account)

            doNotify(message_text)
    except Exception as e:
        print(e)
        print('Error sending email for Root login notifications for {} from bucket {}.'.format(key, bucket))
        raise e

