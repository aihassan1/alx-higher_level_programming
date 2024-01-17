#!/usr/bin/python3
"""document the file 2-filter_states.py"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Ensure code is not executed when imported"""
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=username, db=database_name)
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cursor.execute(
        "SELECT * FROM `states` WHERE BINARY `name` = %s ORDER BY `id` ASC",
        (state_name_searched,),
    )

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
