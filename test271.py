# Inner function can access local variable of outer function directily
# But can not modify or update

def fun1():
    x=100
    y=200
    def fun2():
        print(f'x={x}')
        print(f'y={y}')
    def fun3():
        x=900 #Create Variable x (x is Local Variable of fun3)
        y=1000 # Create Variavble y (y is Local Variable of fun3)
        print(f'x={x}')
        print(f'y={y}')
       

    fun2()
    fun3()
    fun2()
    

fun1()    
