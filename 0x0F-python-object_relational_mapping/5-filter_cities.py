#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Ensure code is not executed when imported"""
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=username, db=database_name)
    cursor = db.cursor()

    # Execute SQL query to select all cities with corresponding state names
    query = (
        "SELECT cities.name "
        "FROM cities "
        "WHERE cities.state_id = ("
        "    SELECT id FROM states WHERE name = %s"
        ") "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (state_name,))

    # Fetch all rows and collect unique city names
    cities = set(row[0] for row in cursor.fetchall())

    # Sort the city names alphabetically
    sorted_cities = sorted(cities)
    # Print the result as a comma-separated string
    print(", ".join(sorted_cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()
