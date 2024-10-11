# Write a program to find nth maximum value

n = int(input("Enter any number: "))
list1=[]
for i in range(n):
    value=int(input("Enter any value: "))
    list1.append(value)
print(list1)

t=int(input("Enter nth maximum value: "))
s=set(list1)
list1=list(s)
list1.sort(reverse=True)
print(f'nth maximum is: {list1[t-1]}')
