# Write a program to print sum of elements of the list

list1=list(range(10,110,10))
print(list1)
s=0
for i in range(len(list1)): #start=0,stop=10,step=1 --> 0 1 2 3 4 5 6 7 8 9
    s=s+list1[i]
print(f'Sum of list1 is: {s}')    
