emp_dict={10:['Rupesh','Developer',100000],
          20:['Uma','Developer',200000],
          30:['Arun','HR',30000],
          40:['Rajesh','Manager',50000],
          50:['Rakesh','Manager',60000]}
print(emp_dict)

emp_dict1={empno:a for empno,a in emp_dict.items() if a[1]=='Manager'}
print(emp_dict1)
emp_dict2={empno:a for empno,a in emp_dict.items() if a[1]=='HR'}
print(emp_dict2)

emp_dict3={empno:a for empno,a in emp_dict.items() if a[1]=='Developer'}
print(emp_dict3)
