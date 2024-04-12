""" SELECT + WHERE """
import pymysql

TABLE_NAME = 'users'
connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
    port=3307
)


with connection:
    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id: '))
        maior_id = int(input('Digite o maior id: '))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s  '
        )

        cursor.execute(sql, (menor_id, maior_id))
        print(cursor.mogrify(sql, (menor_id, maior_id)))
        data = cursor.fetchall()

        for row in data:
            print(row)

    connection.commit()
