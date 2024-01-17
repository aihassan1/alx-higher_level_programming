#!/usr/bin/python3
"""document the file 1-filter_states.py"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Ensure code is not executed when imported"""
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=username, db=database_name)
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cursor.execute(
        "SELECT * FROM states " "WHERE name LIKE 'N%' "
        "ORDER BY states.id ASC"
    )

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
