x=100 # Global Variables
y=200# Global Variables

def fun1():
    #global x,y
    print(x,y)

def fun2():
    x=10 #Local Variable
    y=20 # Local Variable
    print(x,y)

def fun3():
    x=1 #Local Variable
    y=2 #Local Variable
    print(x,y)
   # global x,y # error --> Syntax error as global key word defined after declaring localvariables
    print(x,y)

fun1()
fun2()
fun3()
