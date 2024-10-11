list1=[10,20,30,40,50]
a=iter(list1)
value1=next(a)
value2=next(a)
value3=next(a)
value4=next(a)
value5=next(a)
print(value1,value2,value3,value4,value4,value5)
#value6=next(a)--> Error

list2=list(range(1,101))
b=iter(list2)

for value in b:
    print(value,end=' ')
