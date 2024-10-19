#use case to demonstrate global key word within function
x=100 # Global Variable
y=200 # Global Variable

def fun1():
    print(x,y)

def fun2():
    global x,y
    x=1000
    y=2000
    print(x,y)

def fun3():
    x=10 #L.V
    y=20 #L.V
    print(x,y)


fun1()    
fun2()
fun1()
fun3()
fun1()
