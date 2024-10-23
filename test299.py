#Recursive Functions examples or use case

def fun1(): # CALLED fUNCTION
    print("Inside Function1")


def fun2(): # Calling Function
    fun1() #Nested Function
    print("Inside function2")


fun2()    

# Recursive Function -> calling function and called function both are same
def fun3():
    print("Inside Function 3")
    fun3()

fun3() # runs until maximum depth and gives an error
