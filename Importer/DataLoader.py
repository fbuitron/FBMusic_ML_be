# This object will be in charge of interacting with the API, and storing the objects into the database.

import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="test_py")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM tbl_user")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])

cur.execute("SELECT * FROM tbl_user WHERE user_id > 2")

print("Second one!!!")
# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])

db.close()

