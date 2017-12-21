
from __future__ import print_function

import boto3
import json
from botocore.exceptions import ClientError
from time import gmtime, strftime
from random import randint

def handler(event, context):
  firehoseClient = boto3.client('firehose')
  response = firehoseClient.list_delivery_streams()
  producer = FirehoseProducer()
  producer.start()
  response = json.loads('{"statusCode": "200", "body": "Sent 25000 records to delivery stream successfully"}')
  return response


class FirehoseProducer:
  def __init__(self):
    self.client = boto3.client('firehose')
    self.delivery_stream_name = 'redshift-game-stream'

  def start(self):
    if self.verify_delivery_stream():
      for _ in range(0, 50):
        records = self.generate_data()
        response = self.client.put_record_batch(DeliveryStreamName=self.delivery_stream_name, Records=records)
        if 'ResponseMetadata' in response and 'HTTPStatusCode' in response['ResponseMetadata']\
            and response['ResponseMetadata']['HTTPStatusCode'] == 200:
          print("Sent 500 Records to Delivery Stream Successfully")
        else:
          print("Failed to send records to Delivery Stream, response: %s" % response)
          return

  def generate_data(self):
    # record_time, user_id, game_id, score
    records = []
    record_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    for _ in range(0, 500):  # firehose batch_put supports up to 500 records
      user_id = randint(0, 1000)
      game_id = randint(0, 20)
      score = randint(0, 10000)

      line = b'{0}|{1}|{2}|{3}\n'.format(record_time, user_id, game_id, score)
      records.append({'Data': line})
    return records

  def verify_delivery_stream(self):
    try:
      self.client.describe_delivery_stream(DeliveryStreamName=self.delivery_stream_name)
      return True
    except ClientError, e:
      if 'ResponseMetadata' in e.response and 'HTTPStatusCode' in e.response['ResponseMetadata']:
        if e.response['ResponseMetadata']['HTTPStatusCode'] == 400:
          print ("Delivery Stream named %s not found" % self.delivery_stream_name)
        else:
          print (e)
      return False
