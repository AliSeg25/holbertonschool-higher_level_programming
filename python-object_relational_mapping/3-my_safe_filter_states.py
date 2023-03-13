import MySQLdb
import sys

if __name__ == '__main__':
    # Get arguments from command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_user,
                         passwd=mysql_password,
                         db=db_name)

    # Create cursor object
    cur = db.cursor()

    # Execute query with parameterized query
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch results and print in desired format
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
