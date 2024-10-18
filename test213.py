# Write a program to arrange the values in a dictionary in ascending order for example:
# Original Dictionary ={1:25,2:21,3:23}
# Expected Output= [21,23,25]

dict1={1:25,2:21,3:23}
list1=list(dict1.values())
list1.sort()
print(list1)
