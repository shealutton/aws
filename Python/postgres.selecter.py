#from boto import kinesis
from __future__ import print_function
import psycopg2
import time


sql = open('/home/ec2-user/queries.txt', 'r')
#sql = ['SELECT * FROM testdata limit 2', 'SELECT * FROM testdata limit 300']

conn = psycopg2.connect(host='client.cluster-c1nnapbxgvhy.us-east-1.rds.amazonaws.com', dbname='client', user='client', password='ganges-9302-Wellness')
cur = conn.cursor()

for item in sql:
    t0 = time.time()
    cur.execute(item)
    things = cur.fetchall()
    t1 = time.time()
    print('Items returned:', len(things), 'Elapsed time:', '{0:.6f}'.format(t1 - t0))
conn.commit()
