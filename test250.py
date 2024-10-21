# We cannot write more than one function with the same name , first function will be replaced with 2nd function with same name
def fun1():
    print("Hello")
def fun1(a):
    print("Bye")

fun1(100)    
    
