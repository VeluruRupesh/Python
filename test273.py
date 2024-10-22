def calc(n1,n2,opr): # n1,n2,opr are local variables of calc
    res=None         # res is local variable of calc
    

    def add():
        nonlocal res
        res=n1+n2


    def sub():
        nonlocal res
        res=n1-n2


    def multipy():
        nonlocal res
        res=n1*n2


    def div():
        nonlocal res
        res=n1/n2


    if opr=='+':
        add()
    elif opr=='-':
        sub()
    elif opr=='*':
        multipy()
    elif opr=='/':
        div()
    return res    

 #Main

num1=int(input('Enter First Number: '))
num2= int(input('Enter Second Number: '))
operator= input('Enter Operator: ')
result=calc(num1,num2,operator)
print(f'Result is {num1}{operator}{num2} is: {result:.2f}')
