# Write a program to write even and odd digits
num= int(input("Enter any number: "))
ec=0
oc=0
while num>0:
    r=num%10
    if r%2 ==0:
        ec+=1
    else:
        oc+=1
    num=num//10
print(f'Count of Even numbers in the number is {ec}')    
print(f'Count of Odd numbers in the number is {oc}') 
