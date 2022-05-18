from collections import namedtuple


Employee=namedtuple("Employee",["emp_id", "emp_name", "job_name", "manager_id", "salary", "dep_id"])




Employee1=Employee(10024,"Hadley_Sylvan","QA_Engineer", 9523,1250,4)

Employee2=Employee(10037,"Marcie_Elodie","RnD_Engineer",9012,1500,4)

Employee3=Employee(10164,"Eileen_Candi","RnD_Engineer", 9012,1500,4)

Employee4=Employee(10021,"Floretta_Ike","QA_Engineer", 9523,750,4)

Employee5=Employee(10094,"Gideon_Talia","QA_Engineer", 9567,500,5)





All_Employees=[Employee1, Employee2, Employee3, Employee4, Employee5]
#print(All_Employees)



Total_salary=0
for i in All_Employees:
        Total_salary=Employee1.salary+Employee2.salary+Employee3.salary+Employee4.salary+Employee5.salary

print(Total_salary)


for i in All_Employees:
    if i.salary >=1250:
        print(i.emp_name)
        
for i in All_Employees:
    if i.dep_id ==4:
        print(i.emp_name,i.job_name)


for i in All_Employees:
    if i.manager_id ==9523:
        print(i.emp_name,i.emp_id,sep="\n")
        
        
        
for i in All_Employees:
    if i.job_name =="QA_Engineer":
        print(i.emp_id,i.emp_name,i.salary)
      
