# Write a program to delete a value from the list using del keyword

list1=[10,20,30,40,50]
print(f'Before deleting list is:{list1}')
value=int(input("Enter value to delete: "))
if value in list1:
    for i in range(len(list1)):
        if list1[i]==30:
            del list1[i]
            break
    print(f'After deleting list is: {list1}')
else:
    print("Value not exitis. ")
