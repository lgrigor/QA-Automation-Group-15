import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "guest",
    passwd = "qwerty",
    database = 'Levon_Grigoryan'
)

cursor = db.cursor()

## creating a table called 'employee' in the 'Levon_Grigoryan' database
cursor.execute("""CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    OrderDate VARCHAR(25)
)""")

cursor.execute("""CREATE TABLE Customers (
    CustomerID INT,
    CustomerName VARCHAR(25),
    ContactName VARCHAR(25),
    Country VARCHAR(25)
)""")

cursor.execute("""CREATE TABLE employee (
    emp_id INT,
    emp_name VARCHAR(100),
    job_name VARCHAR(100),
    manager_id INT,
    salary INT,
    dep_id INT)
""")