def fun1(a,b,/,x,y):
    print(a,b,x,y)
fun1(100,200,300,400)    
fun1(100,200,x=500,y=600)
#fun1(a=100,b=200,20,30) #-->runtime error
