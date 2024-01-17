#!/usr/bin/python3
"""
Filter states : script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]


if __name__ == "__main__":
    """code should not be executed when imported"""
    db = MySQLdb.connect(host="localhost", user=username, db=database_name)
    cursor = db.cursor()

    cursor.execute
    ("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
