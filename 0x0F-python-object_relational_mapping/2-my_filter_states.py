#!/usr/bin/python3

import sys
import MySQLdb


def get_states(username, password, db_name, search_value):
    """
        displays all values in the states table of
        hbtn_0e_0_usa where name matches the argument.
    """
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    bad_query = "SELECT * FROM states WHERE name=('{}')\
                 ORDER BY id ASC".format(search_value)
    cursor.execute(bad_query)
    rows = cursor.fetchall()
    for row in rows:
        if (row[1] == search_value):
            print(row)
    cursor.close()
    db.close()
