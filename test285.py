# Write a program to create custom iterator to rwead values from right to left

def riter(iterable): # iterable means list
    for i in range(-1,-(len(iterable)+1),-1):
        yield iterable[i]



list1=[10,20,30,40,50,60,70,80,90,100]
a=iter(list1)
for value in a:
    print(value,end=' ')
print()

b=riter(list1)
for value in b:
    print(value,end=' ')
print()    
    
        
                   
    
