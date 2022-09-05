from sqlite3 import Cursor
import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="", database="phyton_database"
)

cursor = db.cursor()

# Note: We use the fetchall() method, which fetches all rows from the last executed statement.
cursor.execute('SELECT * FROM customers')
allData = cursor.fetchall()

i = 1
while i <= len(allData):
    print(i, allData[i-1])
    i += 1

# SELECTIONG COLUMNS
# To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):

cursor.execute('SELECT name, address FROM customers')
allData = cursor.fetchall()

i = 1
while i <= len(allData):
    print(i, allData[i-1])
    i += 1


# FETCHONE
# If you are only interested in one row, you can use the fetchone() method.
# The fetchone() method will return the first row of the result:

cursor.execute('SELECT * FROM customers ')

firstData = cursor.fetchone()
print(firstData)
