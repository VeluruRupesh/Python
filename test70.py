#immutable
a=10
b=10
print(a==b)
print(a is b)

#mutable
list1=[10,20,30,40,50]
list2= [10,20,30,40,50]
print(list1==list2) #comparing values
print(list1 is list2) #comparing address

list3=list1 #list1 is assigned to list1
print(list1 is list3)
