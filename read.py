""" CRUD >> READ """
import pymysql as db

connection = db.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
    port=3307
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM users'
        )

        for row in cursor.fetchall():
            _id, email, password = row
            print(_id, email, password)

        connection.commit()
