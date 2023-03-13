#!/usr/bin/python3
<<<<<<< HEAD

"""
Lists all states from the database hbtn_0e_0_usa sorted in ascending order by states.id
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

    # Create a cursor object allows to execute
    cursor = db.cursor()

    #Cette ligne exécute une requête SQL qui sélectionne 
    # toutes les lignes de la table "states" dans la base de données 
    # triées par ordre croissant de leur id.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Ces lignes extraient toutes les lignes de résultats 
    # de la requête et les affichent à l'écran.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()

=======
'''States listing module'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3])
    st = db.cursor()
    st.execute("""SELECT `id`, `name` FROM states ORDER BY `id`;""")
    res = st.fetchall()
    for i in res:
        print(i)
    db.close()
>>>>>>> 143f3f0714e0d3ad05316566215efe56a7832bcf
