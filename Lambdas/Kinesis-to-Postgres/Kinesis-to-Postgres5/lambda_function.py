from __future__ import print_function

import base64
import json
import psycopg2


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # Body:
    # 2017-04-20T10:51:35-05:00,1516685,3821752,7352132,224.41.96.118,ge,499.00
    #conn = psycopg2.connect(host='client.crk8x6geh5ji.us-east-1-beta.rds.amazonaws.com', dbname='client', user='client',
    #                        password='ganges-9302-Wellness')
    #cur = conn.cursor()

    sql = 'INSERT INTO testdata (tradeID, firmID, accountID, clearingfirmID, ip, instrument, quantity, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data']).rstrip()
        items = payload.split(',')
        #cur.execute(sql, (items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[8]))
        #conn.commit()
        print(items)
    return 'Successfully processed {} records.'.format(len(event['Records']))
