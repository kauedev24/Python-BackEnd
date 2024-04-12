""" CRUD >> DELETE """
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
        delete_user = input("Digite o id do usuario para ser deletado: ")
        COLUNA = 'id'

        # antes
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        for row in cursor.fetchall():
            print(row)

        sql = (
            f'DELETE FROM {TABLE_NAME} '
            f'WHERE {COLUNA} = (%s)'
        )

        cursor.execute(sql, delete_user)

        # depois
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        for row in cursor.fetchall():
            print(row)

    connection.commit()
