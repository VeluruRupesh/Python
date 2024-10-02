# Write a program to find length od a number or count of digits
#Method-1
n1=input("Enter any Number: ")
x=len(n1)
print(x)

#Method-2
num=int(input("Enter any number: "))
c=0
while num>0:
    c+=1
    num=num//10

print(f'Count of digits or length of number is {c}')    
    
