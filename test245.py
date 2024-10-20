# Funtion with Return Value or return keyword
#syntax: return<value>/<expression>

def add2(a,b):
    c=a+b
    print(f'Sum of {a} and {b} is: {c}')

def add3(a,b):
    c=a+b
    return c
def fun1():
    print("Hello")
    return  # here function terminates and returns to calling place
    print("Bye")

add2(100,200)
res=add3(10,20) # retun value is assigned to res and we can print res value
res1=pow(4,2)
print(res,res1)
fun1()
