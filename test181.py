# Write a program to add two numbers (input validations)
s1 = input("Enter first number: ")
s2= input("Enter second number: ")
if s1.isdigit() and s2.isdigit():
    res=int(s1)+int(s2)
    print(f"Sum of {s1} and {s2} is: {res}")
else:
    print("Input must be integer")
