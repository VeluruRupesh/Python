def smart_division(f):
    def new_div(n1,n2):
        if n2==0:
            return 0
        else:
            f(n1,n2)
    return new_div        


@smart_division # decorator
def div(n1,n2):
    n3=n1/n2
    return n3

num1=int(input("Enter first integer: "))
num2=int(input("Enter second integer: "))
result= div(num1,num2)
print(result)
