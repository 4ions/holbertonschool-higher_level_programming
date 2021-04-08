#!/usr/bin/python3
""" Module that takes in argument and displays all values """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    curse = db.cursor()
    q = """SELECT * FROM states WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC """
    q = q.format(argv[4])
    curse.execute(q)
    query_rows = curse.fetchall()
    for row in query_rows:
        print(row)

    curse.close()
    db.close()
