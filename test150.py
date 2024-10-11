# Write a prrogram to find smallest number in the list
n=int(input("Enter value of n: "))
list1=[]
for i in range(n):
    value=int(input("Enter any value: "))
    list1.append(value)
print(list1)

for i in range(len(list1)):
    if i==0:
        min_value=list1[i]
    elif list1[i]< min_value:
        min_value=list1[i]
print(f'Minimum value in the list1 is: {min_value}')        
    
    
