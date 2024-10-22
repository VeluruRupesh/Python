list1=[1,2,3,4,5,6,7,8,9,10]


a=filter(None,list1)
for value in a:
    print(value,end=' ')
print()
list2=[0,0,0,0,1,2,3,0,0,0,0]
b=filter(None,list2)
for value in b:
    print(value,end=' ')
print()
c=filter(lambda a:a%2==0,list1)
for value in c:
    print(value,end=' ')
