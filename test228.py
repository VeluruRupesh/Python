def fun1():
    a=100 #local variable
    b=200 #local variable
    print(a,b)

def fun2():
    print(a,b) # a,b are local variable of fun1() and cannot be accessed in fun2()

fun1()    
fun2()
