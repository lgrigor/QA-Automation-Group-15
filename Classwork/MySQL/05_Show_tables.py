import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "guest",
    passwd = "qwerty",
    database = 'Levon_Grigoryan'
)

cursor = db.cursor()

## getting all the tables which are present in 'Levon_Grigoryan' database
cursor.execute("SHOW TABLES")

tables = cursor.fetchall() ## it returns list of tables present in the database

## showing all the tables one by one
for table in tables:
    print(table)
