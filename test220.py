# Wrire a program to read the details of n employees.
# Each employee is having empno,ename,salary

n=int(input("Enter How Many Employees: "))
emp={int(input("Enter Empno: ")):[input("Employee Name: "),float(input("Employee Salary: "))] for i in range(n)}
for a,b in emp.items():
    print(f'{a}-->{b}')
    
     
         
         
