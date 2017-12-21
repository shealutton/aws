from __future__ import print_function
import argparse
import sys
import signal
import psycopg2


# db instance ident = client
# master user = <your username here>
# master pass = <your pass here> # If not IAM capable!
# psql -h hostname -U client -d client

# CREATE TABLE testdata (
# code char(5),
# title varchar(40),
# id integer,
# date_prod date default now(),
# kind varchar(10),
# len integer);'


__author__ = "Shea Lutton, 2017"
__version__ = "1.1.0"
__email__ = "shealutt@amazon.com"

parser = argparse.ArgumentParser(description='Postgres Inserter')
parser.add_argument('-s', '--db_server', help='Database server hostname', required=True)
parser.add_argument('-d', '--database',  help='Database name', required=True)
parser.add_argument('-u', '--user',      help='Database user', required=True)
args = parser.parse_args()


def main():
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGHUP, quit)
    insert()


def insert():
    conn = psycopg2.connect(host=args.db_server, dbname=args.database, user=args.user,
                            password="")
    cur = conn.cursor()

    sql = 'INSERT INTO testdata (code, title, id, kind, len) VALUES (%s, %s, %s, %s, %s)'
    # Loop, inserting any data we receive
    while True:
        cur.execute(sql, ('abcde', 'My Title is CIA', 12345, 'kind-1234', 189))
        conn.commit()


def quit(signum, frame):
    print(' Received exit signal. ')
    sys.exit(0)


if __name__ == '__main__':
    main()