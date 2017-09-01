from boto import kinesis
#import testdata
#import json


kinesis = kinesis.connect_to_region("us-east-1")
#kinesis.list_streams()

records = []
count = 0
while count < 100000:
    x = '2,6002978,4924046,9418438,6949100,71.114.74.69,ge,100,165.00'
    record = {'Data': x,'PartitionKey': str(hash(str(count)))}
    records.append(record)
    if count % 400 == 0:
        kinesis.put_records(records, "KinesisToLambda")
        records=[]
    count += 1
kinesis.put_records(records, "KinesisToLambda")
