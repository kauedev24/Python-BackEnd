""" CRUD >> CREATE """
# PyMySQL - um cliente MySQL feito em Python puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql


connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
    port=3307
)

with connection:
    with connection.cursor() as cursor:

        cursor.execute(
            'CREATE TABLE users ('
            'id int(11) NOT NULL AUTO_INCREMENT, '
            'email varchar(255) COLLATE utf8_bin NOT NULL, '
            'password varchar(255) COLLATE utf8_bin NOT NULL, '
            'PRIMARY KEY(id)) '
            'ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_bin '
            'AUTO_INCREMENT = 1'
        )
        connection.commit()
