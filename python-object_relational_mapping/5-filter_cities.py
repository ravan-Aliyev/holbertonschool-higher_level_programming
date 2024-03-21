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
    cursor.execute("select cities.name\
                   from cities left join states on cities.state_id\
                   =states.id where states.name = '{:s}'\
                   order by cities.id".format(sys.argv[4]))

    rows = cursor.fetchall()

    for i, row in enumerate(rows):
        print(row, end=", " if i < len(row) - 1 else "")

    cursor.close()
    connection.close()
