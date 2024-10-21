def fun1(a,c=10,*b):
    print(a,b,c)


fun1(100,200,300,400,500)
#fun1(100,b=200,300,400) with giving value for c we can not give valiues to b
fun1(100,200)
