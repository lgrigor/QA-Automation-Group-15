import csv
from collections import namedtuple

employee = namedtuple("employee", ["emp_id", "emp_name", "job_name", "manager_id", "salary", "dep_id"])
all_employees = []

csv_file = r'C:\Users\User\Desktop\Python Automation\employees.csv'
for i in list(csv.DictReader(open(csv_file))):
    all_employees.append(employee(**i))

#Print the total amount of the salary.
def total_salary ():
    salary = 0
    each_employee: employee
    for each_employee in all_employees:
      salary += int(each_employee.salary)
    print('Total salary of all employees is ' + str(salary))

#Print the names of all employees whose salary is greater than or equal to 1250.
def employee_salary (salary: int):
    each_employee = employee
    for each_employee in all_employees:
        if int(each_employee.salary) >= salary:
            print(each_employee.emp_name)

#Print the names and job names of all employees whose department ID is 4.
def employee_department(department: int):
    each_employee: employee
    for each_employee in all_employees:
        if int(each_employee.dep_id) == department:
            print(each_employee.emp_name, each_employee.job_name)


#Print the names then IDs of all employees whose manager ID is 9523.
def employee_managers(manager_id):
    each_employee: employee
    for each_employee in all_employees:
        if int(each_employee.manager_id) == manager_id:
            print(each_employee.emp_name, ':', each_employee.emp_id) 


#Print the IDs, names, and salaries of all QA engineers.
def employees_position(job_name: str):
    each_employee: employee
    for each_employee in all_employees:
        if each_employee.job_name.lower().strip() == job_name.lower():
            print(each_employee.emp_id, each_employee.emp_name, each_employee.salary)



total_salary()
employee_salary(1250)
employee_department(4)
employee_managers(9523)
employees_position('QA_Engineer')


