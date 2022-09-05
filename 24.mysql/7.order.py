import mysql.connector

db = mysql.connector.connect(
    host="localhost", user='root', password="", database="phyton_database"
)

cursor = db.cursor()

sql = 'SELECT * FROM customers ORDER BY name DESC'
cursor.execute(sql)

result = cursor.fetchall()
for x in result:
    print(x)
