from audioop import add
import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user="root", password='', database='phyton_database'
)
cursor = conn.cursor()

# name = input('Enter your name : ')
# address = input('Enter your address : ')
# phone = input('Enter your phone number :')

# query = 'INSERT INTO customers (name, address, phone) VALUES ("{name}", "{address}", {phone})'
# query = query.format(name=name, address=address, phone=phone)

# cursor.execute(
#     query)

# Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
# conn.commit()

# print(cursor.rowcount, ' Record inserted')


# insert multiple rows
# To insert multiple rows into a table, use the executemany() method.
# The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:

query = 'INSERT INTO customers (name, address, phone) VALUES (%s, %s, %s)'
val = [
    ('Andreas1', 'Address1', 1),
    ('Andreas2', 'Address2', 2),
    ('Andreas3', 'Address3', 3),
    ('Andreas4', 'Address4', 4),
    ('Andreas5', 'Address5', 5),
]

cursor.executemany(query, val)

conn.commit()
print(cursor.rowcount, 'Row inserted.')


# GET INSERTED ID
# todo learn get inserted id
