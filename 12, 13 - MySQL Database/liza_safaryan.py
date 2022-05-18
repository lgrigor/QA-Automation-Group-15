import mysql.connector as mysql

db = mysql.connect(
 host = "80.86.231.141",
 user = "guest",
 passwd = "iM9]M)bS-G",
 database = "liza_safaryan"
)

cursor = db.cursor()

#creating table
cursor.execute("""CREATE TABLE employees (
 emp_name VARCHAR(50),
 job_name VARCHAR(50),
 city_name VARCHAR(15),
 age INT,
 emp_date VARCHAR(15)
 )
 """)

#creating columns
query = "INSERT INTO employees (emp_name, job_name, city_name, age, emp_date) VALUES (%s, %s, %s, %s, %s)"
emps = [('Airi Sato', 'Accountant', 'Tokyo', 33, '2008/11/28'),
("Angelica Ramos", "Chief Executive Officer (CEO)", "London", 47, "2009/10/09"),
("Ashton Cox", "Junior Technical Writer", "San Francisco", 66, "2009/01/12"),
("Bradley Greer", "Software Engineer", "London", 41, "2012/10/13"),
("Brenden Wagner", "Software Engineer", "San Francisco", 28, "2011/06/07")]

cursor.executemany(query, emps)
db.commit()

#deleting line
query = "DELETE FROM employees WHERE job_name REGEXP 'software engineer'"
cursor.execute(query)
db.commit()

#select
query = "SELECT * FROM employees WHERE emp_date REGEXP '/10/'"
cursor.execute(query)
lines = cursor.fetchall()
for line in lines:
    print(line)