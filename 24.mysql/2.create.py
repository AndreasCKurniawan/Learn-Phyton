import mysql.connector

# to create database, use "CREATE DATABASE" statement
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=""
)

print("Connec   ", conn)

myCursor = conn.cursor()

myCursor.execute('CREATE DATABASE phyton_database')

# check if database exist

myCursor.execute('SHOW DATABASE')

for x in myCursor:
    print(x)
