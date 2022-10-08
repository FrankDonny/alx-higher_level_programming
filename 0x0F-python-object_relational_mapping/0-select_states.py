#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY id')
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    conn.close()