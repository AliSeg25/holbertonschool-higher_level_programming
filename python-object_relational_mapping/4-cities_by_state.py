#!/usr/bin/env python3
"""
Lists all cities from the database hbtn_0e_4_usa sorted in ascending
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                   INNER JOIN states ON cities.state_id = states.id \
                   ORDER BY cities.id ASC")

    # Fetch all the rows in a list of lists
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()
