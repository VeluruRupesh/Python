# map() function use case

list1=[1,2,3,4,5,6,7,8,9,10]

p=map(lambda a:a**2,list1)
for value in p:
    print(value,end=' ')

print()
c=map(lambda a:a if a%2==0 else None,list1)
for value in c:
    print(value,end=' ')
