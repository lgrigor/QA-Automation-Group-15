from collections import namedtuple
employee = namedtuple('employee', ['emp_id', 'emp_name', 'job_name', 'manager_id', 'salary', 'dep_id'])
employee1 = employee(10024, "Hadley_Sylvan", "QA_Engineer", 9523, 1250, 4)
employee2 = employee(10037, "Marcie_Elodie", "RnD_Engineer", 9012, 1500, 4)
employee3 = employee(10164, "Eileen_Candi", "RnD_Engineer", 9523, 1500, 4)
employee4 = employee(10021, "Floretta_Ike", "QA_Engineer", 9523, 750, 4)
employee5 = employee(10024, "Gideon_Talia", "QA_Engineer", 9567, 500, 5)
employees = [employee1, employee2, employee3, employee4, employee5]
sum = 0
for i in employees:
    sum += i.salary
print(sum)
for i in employees:
    if i.salary >= 1250:
        print(i.emp_name)
for i in employees:
    if i.dep_id == 4:
        print(i.emp_name, i.job_name, sep = "-")
for i in employees:
    if i.manager_id == 9523:
        print(i.emp_name)
        print(i.emp_id)
for i in employees:
    if i.job_name == "QA_Engineer":
        print(i.emp_id, i.emp_name, i.salary, sep = "-")
