# Write a program to display last digit of the number is divisible by 3 or not.

n1= int(input("Enter any number: "))
last_digit=n1%10
if last_digit%3==0:
    print(f'{last_digit} of {n1} divisable by 3')
else:
    print(f'{last_digit} of {n1} not divisible by 3')
