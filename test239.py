# Function without parameters
def fun1():
    print("Hello")

# Function with parameters
def fun2(a,b): # required arguments
    print(a,b)
fun1()
fun2(10,20) # Required positional arguments
fun2(a=10,b=20) # Required Keyword arguments
fun2(b=100,a=200) #Required keyword arguments
fun2(500,600) # Reuired positional arguments
