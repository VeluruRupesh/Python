def fun1(a,*b,c=10):
    print(a,b,c)



fun1(100)
fun1(100,200,300,400,500)
fun1(100,c=500)
fun1(100,200,300,400,500,c=600)
