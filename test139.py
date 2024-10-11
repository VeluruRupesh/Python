# count even or odd numbers
list1=[4,8,9,11,13,18,46,32,19]
ec,oc=0,0
for value in list1:
    if value%2==0:
        ec+=1       
    else:
        oc+=1
print(f'List is: {list1}')        
print(f'Even count of list is: {ec}')
print(f'Odd count of list is: {oc}')
