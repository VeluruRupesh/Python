# Write a program to find second maximum value

n=int(input("Enter the value of n: "))
list1=[]
for i in range(n):
    value=int(input("Enter any value: "))
    list1.append(value)
print(list1)

list1.sort()
c=list1.count(max(list1))

print(f'Second Maximum value is: {list1[-(c+1)]}')


n=int(input("Enter the value of n: "))
list1=[]
for i in range(n):
    value=int(input("Enter any value: "))
    list1.append(value)
print(list1)

list1.sort(reverse=True)
c=list1.count(max(list1))

print(f'Second Maximum value is: {list1[c]}')
