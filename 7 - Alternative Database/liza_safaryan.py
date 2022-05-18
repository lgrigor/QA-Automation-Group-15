from collections import namedtuple
employee = namedtuple('employee', ['emp_id', 'emp_name', 'job_name', 'manager_id', 'salary', 'dep_id'])

emp_id: int
emp_name: str
job_name: str
manager_id: int
salary: int
dep_id: int

emp1 = employee(10024, 'Hadley_Sylvan', 'QA_Engineer', 9523, 1250, 4)
emp2 = employee(10037, 'Marcie_Elodie', 'RnD_Engineer', 9012, 1500, 4)
emp3 = employee(10164, 'Eileen_Candi', 'RnD_Engineer', 9012, 1500, 4)
emp4 = employee(10021, 'Floretta_Ike', 'QA_Engineer', 9523, 750, 4)
emp5 = employee(10094, 'Gideon_Talia', 'QA_Engineer', 9567, 500, 5)

emp_list = [emp1, emp2, emp3, emp4, emp5]


# 1. Print the total amount of the salary.
total_salary = 0
for y in emp_list:
    total_salary += y.salary
print(f"1. The total amount of the salary is {total_salary}\n")


#2. Print the names of all employees whose salary is greater than or equal to 1250.
print("2. Employees whose salary is greater than or equal to 1250: ")
for n in emp_list:
    if n.salary >= 1250:
        print(f"{n.emp_name}")


#3. Print the names and job names of all employees whose department ID is 4.
print("\n3. Employees whose department ID is 4")
for x in emp_list:
    if x.dep_id == 4:
        print(f"{x.emp_name} - {x.job_name}")


#4. Print the names then IDs of all employees whose manager ID is 9523.
print("\n4. Employees with manager ID 9523")
for x in emp_list:
    if x.manager_id == 9523:
        print(f"{x.emp_name} - {x.emp_id}")


#5. Print the IDs, names, and salaries of all QA engineers.
print("\n5. All QA engineers")
for x in emp_list:
    if x.job_name == "QA_Engineer":
        print(f"{x.emp_id} - {x.emp_name} - {x.salary}")
