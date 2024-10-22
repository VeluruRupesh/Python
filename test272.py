# nonloal keyword is used to update or modify the fun1() local variables or outer function variables
def fun1():
    x=100 # Local Variable of fun1()
    y=100 # Local Variable of fun1()
    def fun2():
        print(f'x={x}')
        print(f'y={y}')
    def fun3():
        nonlocal x,y
        x=888
        y=999
        print(f'x={x}')
        print(f'y={y}')

    fun2()
    fun3()
    fun2()

fun1()    
