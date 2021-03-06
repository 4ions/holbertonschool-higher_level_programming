#!/usr/bin/python3
""" Module list all states and with injections protections """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name = %s ORDER BY
                    states.id ASC""", (argv[4],))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
