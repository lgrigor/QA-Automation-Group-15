from collections import namedtuple
import csv

def total_salary():
    """Print the total salary of all employees"""
    total_salary = 0
    each_employee: employee
    for each_employee in all_employees:
        total_salary += int(each_employee.salary)
    print(total_salary)

def employees_salary(salary: int):
    """Print the names of all employees whose salary is greater than or equal {salary}"""
    each_employee: employee
    for each_employee in all_employees:
        if int(each_employee.salary) >= salary:
            print(each_employee.emp_name)

def employees_department(dep_id: int):
    """Print the names and job names of all employees whose department ID is {dep_id}"""
    each_employee: employee
    for each_employee in all_employees:
        if int(each_employee.dep_id) == dep_id:
            print(each_employee.emp_name, each_employee.job_name)

def employees_manager(man_id: int):
    """Print the names then IDs of all employees whose manager ID is {man_id}"""
    each_employee: employee
    for each_employee in all_employees:
        if int(each_employee.manager_id) == man_id:
            print(each_employee.emp_name, each_employee.emp_id)

def employees_position(position: str):
    """Print the IDs, names, and salaries of all {position}"""
    each_employee: employee
    for each_employee in all_employees:
        if each_employee.job_name.lower() == position.lower():
            print(each_employee.emp_id, each_employee.emp_name, each_employee.salary)

employee = namedtuple("employee", ["emp_id", "emp_name", "job_name", "manager_id", "salary", "dep_id"])
all_employees = []

for i in list(csv.DictReader(open("data/employees.csv"))):
    all_employees.append(employee(**i))

### Uncomment below to see the result
# total_salary()
# employees_salary(1250)
# employees_department(4)
# employees_manager(9523)
# employees_position('qa_engineer')
