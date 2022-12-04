#!/usr/bin/python3

import sys
import MySQLdb


def get_states(username, password, db_name):
    """
         lists all states with a name starting with N from the database
    """
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`\
                   WHERE `name` REGEXP '^N' ORDER BY `id` ASC")
    rows = cursor.fetchall()
    for row in rows:
        if ("N" in row[1]):
            print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3])
