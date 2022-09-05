import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='', database='phyton_database'
)
cursor = db.cursor()

# DELETE RECORD
# 'DELETE FROM'
sql = 'DELETE FROM customers WHERE name = "Andreas5"'
cursor.execute(sql)

sql = 'SELECT * FROM customers ORDER BY name '
cursor.execute(sql)
result = cursor.fetchall()

for x in result:
    print(x)

db.commit()

# PREVENT SQL INJECTION
# The mysql.connector module uses the placeholder %s to escape values in the delete statement:

sql = 'DELETE FROM customers WHERE name = "%s"'
value = ('Andreas4',)
cursor.execute(sql, value)

sql = 'SELECT * FROM customers'
cursor.execute(sql)

result = cursor.fetchall()
for x in result:
    print(x)
