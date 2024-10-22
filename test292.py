# Predefined functions of lambda functions use cases
list1=[1,3,4,8,9,12,56,87,47,23,33,65,76,45,32,11,22,89,67,87,65,45]
x=filter(lambda a:a%2==0,list1)
for value in x:
    print(value,end=' ')
print()
y=filter(lambda a:a%2!=0,list1)
for value in y:
    print(value,end=' ')

print()
z=filter(lambda a:a%2==0,list1)
list1=list(z)
print(list1)
    
