from __future__ import print_function
import psycopg2
import time
import signal
import sys


# The connection timeout is key here in the connection parameters.
def connect_loop():
    conn = psycopg2.connect(host='', dbname='', user='', password='', connect_timeout=1)
    cur = conn.cursor()
    sql = 'select nspname from pg_catalog.pg_namespace'
    cur.execute(sql)
    cur.close()
    conn.close()


def logic_loop():
    print('Starting connection')
    while True:
        try:
            connect_loop()
        except:
            t0 = time.time()
            break
    #print('Disconnected at', t0, 'Starting reconnect')

    while True:
        try:
            connect_loop()
            t1 = time.time()
            break
        except:
            pass
    #print('Reconnected at', t1, 'Total outage', t1-t0)
    return (t1-t0)


def quit(signum, frame):
    print(' Received exit signal. ')
    sys.exit(0)


def main():
    cumulative_time = 0
    for i in range(10):
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGHUP, quit)
        cumulative_time += logic_loop()
        print('Trial', i, 'Cumulative time:', cumulative_time)


if __name__ == '__main__':
    main()
