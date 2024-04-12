""" CRUD >> UPDATE """

import pymysql

TABLE_NAME = 'users'
connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
    port=3307
)

# atualizando nomes de usuarios
with connection:
    with connection.cursor() as cursor:
        COLUMN = 'name'
        new_name = input('Atualize seu nome: ')
        user_id = int(input("Digite o id do usuário: "))

        # antes
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        data = cursor.fetchall()

        for row in data:
            print(row)

        sql = (
            f'UPDATE {TABLE_NAME} '
            f'SET {COLUMN} = %s '
            'WHERE id = %s'
        )

        cursor.execute(sql, (new_name, user_id))

        # depois
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        data = cursor.fetchall()

        for row in data:
            print(row)

    connection.commit()
