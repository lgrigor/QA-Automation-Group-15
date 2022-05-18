import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "guest",
    passwd = "qwerty"
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'Levon_Grigoryan'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create the 'Levon_Grigoryan' database cursor.execute("CREATE DATABASE Levon_Grigoryan")
cursor.execute("CREATE DATABASE Levon_Grigoryan")