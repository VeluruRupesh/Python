# Inner function can access local data of outer function

def fun1(): # Outer Function
    x=100 # Local Variable
    def fun2(): #Inner Function
        print(f'Local Variable of fun1 is : {x}')
    fun2()

fun1()
    
