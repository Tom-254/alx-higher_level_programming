#!/usr/bin/python3
import sys
import MySQLdb


def get_states(username, password, db_name):
    """
        lists all cities from the database hbtn_0e_4_usa
    """
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM `cities`\
                    JOIN `states` ON state_id=states.id\
                    ORDER BY cities.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3])
