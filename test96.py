# Write  program to print sum of digits of input number

num= int(input("Enter any number: "))
s=0
while num>0:
    r=num%10
    s+=r
    num=num//10
print(f'Sum of digits of input number is {s}')    
    
