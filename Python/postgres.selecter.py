from __future__ import print_function
import psycopg2
import time


sql = open('/home/ec2-user/queries.txt', 'r')

conn = psycopg2.connect(host='', dbname='', user='', password='')
cur = conn.cursor()

for item in sql:
    t0 = time.time()
    cur.execute(item)
    things = cur.fetchall()
    t1 = time.time()
    print('Items returned:', len(things), 'Elapsed time:', '{0:.6f}'.format(t1 - t0))
conn.commit()
