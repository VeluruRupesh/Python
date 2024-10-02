# Write s program to find a person is eligible to vote or not
#Input
#Name
#Age

name= input("Enter Name: ")
age= int(input("Enter Age: "))
result= f'{name} is eligible to vote'if age >=18 else f'{name} is not eligile to vote'
print(result)
