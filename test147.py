# Write a program to swap 2 elements in the list.
#Given a list in the Python and provided the positions of the elements,
#write a program to swap the two elements in the list.
#example: input: list=[23,65,19,90] , pos1 =1 , pos2=3
#output: [19,65,23,90]

n= int(input("Enter how many values? "))
list1=[]

for i in range(n):
    value=int(input("Enter any values: "))
    list1.append(value)
print(f"Before swaping list1 is: {list1}")

p1=int(input("Enter position1: "))
p2=int(input("Enter position2: "))

list1[p1-1],list1[p2-1]=list1[p2-1],list1[p1-1]


print(f'After Swaping list1 is: {list1}')
