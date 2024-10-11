# Write a program to sort the elements of the list in the ascending order

n=int(input("Enter value of n: "))

list1=[]

for i in range(n):
    value=int(input("Enter any value: "))
    list1.append(value)
print(f'Before sorting the list is: {list1}')

for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(f'After swaping the list1 is: {list1}')        
