#Find factorial of input number using function recursion

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

number=int(input("Enter Any number: "))
res=factorial(number)

print(f'Factorial of {number} is: {res}')
