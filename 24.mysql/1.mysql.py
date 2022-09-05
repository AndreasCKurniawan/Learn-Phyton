import mysql.connector

# create connection
conn = mysql.connector.connect(
    host='localhost', user='root', password=""
)

print(conn)
