def fun1(): #Outer Function
    print("Insider outer function")
    def fun2(): #Inner function
        print("Inside inner Function")
    fun2()# calling fun2()    

fun1() # calling fun1()


        
