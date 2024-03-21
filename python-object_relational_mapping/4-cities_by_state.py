#!/usr/bin/python3
"""Connectio to database"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cursor = connection.cursor()
    cursor.execute("select cities.id, cities.name, states.name\
                   from cities left join states on cities.state_id\
                   =states.id order by cities.id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
