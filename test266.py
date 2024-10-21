def fun1(*vargs,**kwargs):
    #*vargs = variable length arguments
    #**kwargs= Keyword arguments
    print(vargs,kwargs)

fun1()
fun1(10,20,30,40,50)
fun1(a=10,b=20,c=30,d=40,e=50)
fun1(10,20,a=30,b=40,c=50)
#fun1(a=10,b=20,30,40,50) -> error -> positional arguments follows keyword arrguments

