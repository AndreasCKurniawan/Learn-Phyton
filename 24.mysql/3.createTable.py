# CREATING TABLE
from audioop import add
import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user="root", password="", database='phyton_database'
)

cursor = conn.cursor()

# cursor.execute(
#     'CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255), phone int(255))')

# cursor.execute(
#     'CREATE TABLE product (name VARCHAR(255), id INT(255), price INT(255))'
# )

# cursor.execute('SHOW TABLES')

# for x in cursor:
#     print(x)

# When creating a table, you should also create a column with a unique key for each record.
# This can be done by defining a PRIMARY KEY.
# We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.

# cursor.execute(
#     'CREATE TABLE store (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')

# If the table already exists, use the ALTER TABLE keyword:
# cursor.execute(
#     "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# cursor.execute('DROP TABLE customers, product, store')
# print(cursor.execute('SHOW TABLES'))

# for x in cursor:
#     print(x)
