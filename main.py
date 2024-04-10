"""."""
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

cursor = connection.cursor()

cursor.close()
connection.close()
