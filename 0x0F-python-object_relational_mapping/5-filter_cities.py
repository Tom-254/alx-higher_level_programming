#!/usr/bin/python3
import sys
import MySQLdb


def get_states(username, password, db_name, state_name):
    """
        lists all cities from the database from a specific state.
    """
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
                    FROM `cities`\
                    JOIN `states` ON state_id=states.id\
                    WHERE states.name=(%s)\
                    ORDER BY cities.id", (state_name,))
    rows = cursor.fetchall()
    cities = ""
    for row in rows:
        for col in row:
            cities += (col) + ", "
    print(cities[:-2])
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
