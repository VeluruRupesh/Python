# Arbitrary Keyword Arguments

def fun1(**a):
    print(a,type(a))



fun1()
fun1(a=10,b=20)
fun1(a=100,b=200,c=300,d=400)
fun1(rollno=1,name='Rupesh',course='Python',fee='5000')
