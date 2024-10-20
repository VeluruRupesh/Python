x=100 # Global Variables
y=200 # Global Variables

def fun1():
    a=globals()
    print(a)
    print(a['x'],a['y'])
    print(x,y)

def fun2():
    x=10 # Local Variables
    y=20 # Local Variables
    print(x,y)
    g=globals()
    print(g['x'],g['y'])

def fun3():
    x=10
    y=20
    z=globals()
    z['x']=500
    z['y']=600
    print(x,y)
    print(z['x'],z['y'])
   
fun1()    
fun2()
fun3()
