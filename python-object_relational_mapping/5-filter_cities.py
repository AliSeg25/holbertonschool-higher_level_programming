#!/usr/bin/env python3
"""
task5
"""
import sys
import MySQLdb


if len(sys.argv) != 5:
    print("Usage: {} <username> <password> <database name> <state name>"
          .format(sys.argv[0]))
    sys.exit(1)

username, password, database, state = sys.argv[1:]

db = MySQLdb.connect(user=username, passwd=password, db=database,
                     host="localhost", port=3306)
cur = db.cursor()

query = "SELECT cities.name FROM cities JOIN states ON cities.state_id =\
states.id WHERE states.name = %s ORDER BY cities.id ASC"
cur.execute(query, (state,))
rows = cur.fetchall()

if rows:
    print(", ".join([row[0] for row in rows]))
else:
    print("No cities found for state '{}'".format(state))

cur.close()
db.close()
