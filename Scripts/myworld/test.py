import sqlite3

conn = sqlite3.connect('db.sqlite3')
my_cursor = conn.cursor()
my_cursor.execute('select * from django_migrations')
p = my_cursor.fetchall()

x = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964',
}
# for a, b in x.items():
    # print(a, b)
# for x in p:
#     # print(x)
# print(p)
