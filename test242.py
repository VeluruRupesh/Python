def fun1(a,b,*,x,y):
    print(a,b,x,y)

def fun2(a,b,/,*,x,y):
    print(a,b,x,y)
    
#fun1(1,2,3,4) #TypeError: fun1() takes 2 positional arguments but 4 were given   
fun1(1,2,x=3,y=4)
fun1(a=100,b=200,x=400,y=500)

fun2(100,200,x=300,y=400)
#fun2(a=1,b=2,3,4) #Runtime Error

#fun2(a=1,b=2,x=3,y=4) #TypeError: fun2() got some positional-only arguments passed as keyword arguments: 'a, b'

fun2(1,2,x=3,y=4)
