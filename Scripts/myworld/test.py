# import sqlite3

# conn = sqlite3.connect('db.sqlite3')
# my_cursor = conn.cursor()
# my_cursor.execute('select * from django_migrations')
# p = my_cursor.fetchall()

# x = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': '1964',
# }
# # for a, b in x.items():
#     # print(a, b)
# # for x in p:
# #     # print(x)
# # print(p)
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
)
my_cursor = mydb.cursor()
sql = "select * from world.country limit 2"

columns = my_cursor.description

print(columns)
my_cursor.execute(sql)
my_result = my_cursor.fetchall()
