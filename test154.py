# Write a program to count each element exist in list
# input: [1,2,3,4,1,1,2,2]
# output
#1-->3
#2-->3
#3-->1
#4-->1

list1=[1,2,3,4,1,1,2,2]
list2=[]
for value in list1:
    if value not in list2:
        list2.append(value)
print(list2)
for value in list2:
    c=list1.count(value)
    print(f'{value}-->{c}')
