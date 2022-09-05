import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="", database="phyton_database"
)

cursor = db.cursor()

cursor.execute('SELECT * FROM customers WHERE name="Andreas1"')
result = cursor.fetchall()

for x in result:
    print(x)

# WHILDCARD CHARACTERS
# You can also select the records that starts, includes, or ends with a given letter or phrase.
# Use the %  to represent wildcard characters:

cursor.execute('SELECT * FROM customers WHERE name LIKE "%eas1%"')
result = cursor.fetchall()

for x in result:
    print(x)

# PREVENT SQL INJECTION
# When query values are provided by the user, you should escape the values.
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# The mysql.connector module has methods to escape query values:

sql = 'SELECT * FROM customers WHERE address = %s'
addr = ('Address1',)

cursor.execute(sql, addr)

result = cursor.fetchall()
for x in result:
    print(x)
