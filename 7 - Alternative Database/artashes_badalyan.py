#Task.1
from collections import namedtuple





Employee = namedtuple('Employee',["emp_id","emp_name", "job_name", "manager_id","salary","dep_id"])   

Emp1 = Employee(10024,"Hadley_Sylvan","QA_Engineer",9523,1250,4)                      

Emp2 = Employee(10037,"Marcie_Elodie","RnD_Engineer",9012,1500,4)

Emp3 = Employee(10164,"Eileen_Candi","RnD_Engineer",9012,1500,4)

Emp4 = Employee(10021,"Floretta_Ike","QA_Engineer",9523,750,4)

Emp5 = Employee(10094,"Gideon_Talia","QA_Engineer",9567,500,5)

print(int(Emp1.salary) +  + int(Emp2.salary) + int(Emp3.salary) + int(Emp4.salary) + int(Emp5.salary))


#task2
for Emps in (Emp1,Emp2,Emp3,Emp4,Emp5):

    if Emps.salary >= 1250:

        print(Emps.emp_name)

#task.3


for Emps in (Emp1,Emp2,Emp3,Emp4,Emp5):

    if Emps.dep_id == 4:

        print(Emps.emp_name,Emps.job_name)        

#Task.4

for Emps in (Emp1,Emp2,Emp3,Emp4,Emp5):
    if Emps.manager_id == 9523:
        print(Emps.emp_name)
        print(Emps.emp_id)

#Task.5 
for Emps in (Emp1,Emp2,Emp3,Emp4,Emp5):
    if Emps.job_name == "QA_Engineer":
        print(Emps.emp_id,Emps.emp_name,Emps.salary)