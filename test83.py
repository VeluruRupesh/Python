# A compay decided to give bonus to an employee

sal=float(input("Enter Salary: "))
service= int(input("Enter employee service(In Years): "))
if service >10:
    bonus=(sal*10/100)
elif service>=6 and service<=8:
    bonus=(sal*8/100)
else:
    bonus=(sal*5/100)

print(f'Salary: {sal:.2f}')
print(f'Service: {service}')
print(f'Net Bonus: {bonus}')
