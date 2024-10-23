# Lambda -> reduce funtion use case or example
#import functiontools to use reduce(fucntools.reduce(function,iterable[,initializer])
import functools
list1=list(range(10,110,10))
print(list1)

res1=functools.reduce(lambda x,y:x+y,list1)
print(res1)

res2=functools.reduce(lambda x,y:x+y,list1,100) # 100 is initilvalue
print(res2)

list2=[]
res3=functools.reduce(lambda x,y:x+y,list2,10)
print(res3)

res4=functools.reduce(lambda x,y:x if x>y else y,list1)
print(res4)

res5=functools.reduce(lambda x,y:x if x<y else y,list1)
print(res5)

res6=functools.reduce(lambda x,y:str(x)+','+str(y),list1)
print(res6,type(res6))
