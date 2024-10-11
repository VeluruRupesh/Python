# Write a program to find largest number in the list

n= int(input("Enter value of n: "))
list1=[]

for i in range(n):
    value=int(input("Enter any value: "))
    list1.append(value)
print(list1)

for i in range(len(list1)):
    if i==0:
        max_value=list1[i]
    elif list1[i]>max_value:
        max_value=list1[i]
print(f'Maximum value of list1 is: {max_value}')        
        
        
