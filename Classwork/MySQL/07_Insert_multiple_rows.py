import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "guest",
    passwd = "qwerty",
    database = 'Levon_Grigoryan'
)

cursor = db.cursor()

# ----------------------- ORDERS -------------------------- 

query = "INSERT INTO Orders (OrderID, CustomerID, OrderDate) VALUES (%s, %s, %s)"
values = [
    (10308, 2, '1996-09-18'),
    (10309, 37, '1996-09-19'),
    (10310, 77, '1996-09-20')
]

cursor.executemany(query, values)
db.commit()
print(cursor.rowcount, "record inserted into Orders")



# ----------------------- CUSTOMERS -------------------------- 

query = "INSERT INTO Customers (CustomerID, CustomerName, ContactName, Country) VALUES (%s, %s, %s, %s)"
values = [
    (1, 'Alfreds Futterkiste', 'Maria Anders', 'Germany'),
    (2, 'Ana Trujillo', 'Emparedados y helados', 'Mexico'),
    (3, 'Antonio Moreno', 'Taquería	Antonio Moreno', 'Mexico')
]

cursor.executemany(query, values)
db.commit()
print(cursor.rowcount, "record inserted into Customers")

# ----------------------- EMPLOYEE -------------------------- 

query = "INSERT INTO employee (emp_id, emp_name, job_name, manager_id, salary, dep_id ) VALUES (%s, %s, %s, %s, %s, %s)"
values = [
    (10037, "Marcie_Elodie", "RnD_Engineer", 9012, 1500, 4),
    (10164, "Eileen_Candi", "RnD_Engineer", 9012, 1500, 4),
    (10021, "Floretta_Ike", "QA_Engineer", 9523, 750, 4),
    (10094, "Gideon_Talia", "QA_Engineer", 9567, 500, 5)
]

cursor.executemany(query, values)
db.commit()
print(cursor.rowcount, "record inserted into employee")