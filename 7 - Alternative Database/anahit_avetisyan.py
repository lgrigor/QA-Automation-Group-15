from collections import namedtuple

student = namedtuple ('Student',['emp_id', 'emp_name', 'job_name','manager_id', 'salary','dep_id'])

Handley_Sylvan = student ( 10024, 'Handley Sylvan', 'QA_Engineer', 9523,1250,4)

Marcie_Elodie = student ( 10037, 'Marcie Elodie', 'RnD_Engineer', 9012,1500,4)

Eileen_Candi = student (10164, 'Eileen Candi', 'RnD_Engineer', 9012,1500,4)

Floretta_Ike = student(10021, 'Floretta Ike', 'QA_Engineer', 9523,750,4)

Gideon_Talia = student(10094, 'Gideon Talia', 'QA_Engineer', 9567,500,5)

print(Handley_Sylvan.salary+ Marcie_Elodie.salary+Eileen_Candi.salary+ Floretta_Ike.salary+ Gideon_Talia.salary)

list = Handley_Sylvan,Marcie_Elodie,Eileen_Candi,Floretta_Ike,Gideon_Talia
print(list)

for i in list:
    if i.salary >= 1250:
        print(i.emp_name)

for i in list:
    if i.dep_id == 4:
        print(i.emp_name, i.job_name)

for i in list:
    if i.manager_id == 9523:
        print(i.emp_name, i.emp_id)

for i in list:
    if i.job_name == 'QA_Engineer':
        print(i.emp_id, i.emp_name, i.salary)


