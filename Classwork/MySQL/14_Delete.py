import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "guest",
    passwd = "qwerty",
    database = 'Levon_Grigoryan'
)

cursor = db.cursor()

## defining the Query
query = "DELETE FROM employee WHERE emp_id = 10021"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()