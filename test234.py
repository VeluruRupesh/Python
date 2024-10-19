num1=100 #Global Variable

def fun1():
    num2=200 #Local Variable
    print(num1,num2)

def fun2():
    num1=500 #Local variable
    print(num1)

fun1()
fun2()  
fun1()

