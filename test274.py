# Use case of LEGB (variables scope of earching)
x=100 #Global Variable
def fun1(): # Outter Function
    y=200 # Local Variable of fun1
    def fun2(): #Inner Function
        z=300 # Loval Variable of fun2
        print(x)  # 1st it looks for x at local and enclosed and global
        print(y) # looks at local variable and enclosed ( i.e fun1())
        print(z) # looks for local variable and z is in local variable of fun2()
        #print(p) # Not in local,enclosed,global built-in also not present -> error: Name error
    fun2()
    
fun1()        
