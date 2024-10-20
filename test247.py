# Write a program to receive and return values using caluculator

def calc(a,b,opr,/):
    match(opr):
        case'+':
            return a+b
        case'-':
            return a-b
        case'*':
            return a*b
        case'/':
            return a/b
        case'//':
            return a//b
        case _:
            return None
#Main
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
Operator=input("Enter first number: ")
result=calc(num1,num2,Operator)
print(f'{num1}{Operator}{num2} is: {result:.2f}')
