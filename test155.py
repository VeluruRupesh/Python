# Write a program to remove duplicate values in the list without converting into
# a set?

list1=[1,2,3,2,3,4,5,6,2,3,4,5,6,7]
list2=[]
for value in list1:
    if value not in list2:
        list2.append(value)
print(list1)        
print(list2)        
