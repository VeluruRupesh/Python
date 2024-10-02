# Write a program to find max of 3 numbers

n1= int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))
n3= int(input("Enter 3rd Number: "))
result = n1 if n1>=n2 and n1>=n3 else n2 if n2>=n1 and n2>=n3 else n3 
print(f'maximum value is {result}')
