def fun1(a,b,/): # / (at the end of arguments)represnts positional only arguments
    print(a,b)

def fun2(*,a,b): # * (at the start of arguments) represnts keyword only arguments
    print(a,b)
def fun3(a,b): # it allows positional as well as keyword
    print(a,b)
    
fun1(10,20)    
#fun1(a=10,b=20) #TypeError: fun1() got some positional-only arguments passed as keyword arguments: 'a, b'

#fun2(10,20) #TypeError: fun2() takes 0 positional arguments but 2 were given
fun2(a=10,b=20)

fun3(200,300)
fun3(a=500,b=600)
