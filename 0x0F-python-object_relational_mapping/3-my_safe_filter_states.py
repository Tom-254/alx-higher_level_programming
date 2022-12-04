import sys
import MySQLdb


def get_states(username, password, db_name, search_value):
    """
        displays all values in the states table of
        hbtn_0e_0_usa where name matches the argument.
        safe from Sql injection.
    """
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`\
                   WHERE `name`=(%s) ORDER BY `id` ASC", (search_value,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
