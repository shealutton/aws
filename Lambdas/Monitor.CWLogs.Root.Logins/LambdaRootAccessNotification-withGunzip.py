###############################################################################
# Lambda function code for Root Access Notification
# 
# This function responds to a S3 Bucket PutObject event.
# The function, required roles and the SNS topic are created via a CF template.
#

from __future__ import print_function

import json
import urllib
import boto3
import re
import gzip
import StringIO

#BOTO SDK Client for SNS
snsClient = boto3.client('sns')

#Mapping list for P&G account numbers-names (needs to be updated if new accounts are created)
accounts = {
    "134628835163":"PG-Enterprise",
    "366222307368":"PG-Enterprise-NonProd",
    "324722364132":"PG-Security",
    "459235286243":"PG-Security-NonProd",
    "633288119929":"PG-Shared-Services",
    "836324581605":"PG-External",
    "816732240656":"PG-External-NonProd",
    "275302624880":"PG-Payer",
    "003499547086":"PG-Sandbox"
    }

#The ARN of the SNS Topic which delivers the email notification, pre-created via CF template
snsARN = 'arn:aws:sns:us-east-1:324722364132:RootAccessNotification'

#The subject line for the email notification to be sent
emailSubject = 'ALERT: Root Account Activity'

#Regular expression that looks for Root account user
rootRegEx = r"arn:aws:iam:\w?:(\d+):root"


#Email notification function
def doNotify(message):
    
    #Publishes the message via the SNS topic
    response = snsClient.publish(Subject=emailSubject, TargetArn=snsARN, Message=message)


#Main function which responds to the S3 PutObject event
def lambda_handler(event, context):

    #Get bucket name and object key from event parameter
    #See sample in file LambdaTestEvent.txt
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    
    try:
        #Get the new file that was put into the S3 bucket (*.json.gz)
        s3 = boto3.resource('s3')
        obj = s3.Object(bucket_name, object_key)
        
        #Get the whole body of the trail file from S3 bucket
        f = StringIO.StringIO()
        obj.download_fileobj(f)
        f.seek(0)
        
        #Uncompress the file content and jsonify
        gzf = gzip.GzipFile(fileobj=f)
        contents = gzf.read()
        contents = json.loads(contents)
        
    except Exception as e:
        print('Error getting the object from S3 bucket or parsing the JSON file.')
        print(e)
        raise e

    try:
        root_login_found = False
        root_accounts = set()

        #Reads each line in the JSON file contents
        #See sample in file 003499547086_CloudTrail_us-west-2_20170331T1935Z_edjqVyE7FrpLwlag.json.gz
        for line in contents['Records']:
            
            #Sees if there's a match with regular expression
            line_string = str(line)
            
            match = re.search(rootRegEx, line_string)
            
            if match:
                #print('Root login found for account:', match.group(0), match.group(1))
                root_login_found = True
                root_accounts.add(match.group(1))

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(object_key, bucket_name))
        raise e
    
    try:
        #Creates the message for the notification
        if root_login_found:
            message_text = 'Activity has been detected under Root login in the following account(s):'
            
            for account in root_accounts:
                message_text = '{0}, {1} ({2})'.format(message_text, accounts[account], account)

            doNotify(message_text)
    except Exception as e:
        print('Error sending email for Root login notifications for {} from bucket {}.'.format(object_key, bucket_name))
        print(e)
        raise e

