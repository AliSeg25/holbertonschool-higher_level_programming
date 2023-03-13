#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY id ASC".format(search_name)
    cursor.execute(query)

    # Fetch all the rows and print them one by one
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()
