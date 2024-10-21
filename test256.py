# Arbitary parameters (paramenters with more than one variables
def add9(a,b):
    c=a+b
    return c

res1=add9(10,20)
print(res1)

def add11(a,b,c):
    z=a+b+c
    return z

res2=add11(10,20,30)
print(res2)

def add12(a,b,c,d):
    e=a+b+d+d
    return e

res3=add12(10,20,30,40)
print(res3)

# arbitary function

def add9(*a):
    print(a)
add9(10,20,30)    

def fun1(*a):
    print(a,type(a),len(a))

fun1()
fun1(10)
fun1(10,20)
fun1(10,20,30,40,50)
fun1(10,'Ruüpesh','Python',0)
    
