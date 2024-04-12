""" INSERT """
import pymysql as db

TABLE_NAME = 'users'

connection = db.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
    port=3307
)

with connection:
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (name, value) VALUES (%s, %s) '
        )
        data4 = (
            ("Siri", 22, ),
            ("Helena", 15, ),
        )
        result = cursor.executemany(sql, data4)
    connection.commit()

# with connection:
#     with connection.cursor() as cursor:
#         cursor.execute(
#             'INSERT INTO users (email, password) VALUES'
#             '("ROBERTA SILVA BRASIL", "111111111"), '
#             '("MARIA SILVA BRASIL", "22222222222"), '
#             '("GABRIELA PEREIRA LIMA", "3333333333"), '
#             '("MARCOS PEREIRA BRASIL", "44444444"), '
#             '("HEMERSON SILVA BRASIL", "999999999")'
#         )

#         connection.commit()

    # with connection.cursor() as cursor:
    #     sql = (
    #         f'INSERT INTO {TABLE_NAME} (name, value) VALUES (%s, %s)'
    #     )
    #     data = ('no sql injection', '25')
    #     cursor.execute(sql, data)
    # connection.commit()

    # with connection.cursor() as cursor:
    #     sql = (
    #         f'INSERT INTO {TABLE_NAME} (name, value) VALUES (%(name)s, %(age)s)'
    #     )
    #     data3 = (
    #         {"name": "Sah", "age": 33, },
    #         {"name": "Júlia", "age": 74, },
    #         {"name": "Rose", "age": 53, },
    #     )
    #     result = cursor.executemany(sql, data3)
    # connection.commit()
