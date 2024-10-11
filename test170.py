# Adding tuple to list and vice-versa
list1=[1,2,3,4,5]
tuple1=(6,7,8,9,10)

list2=list1+list(tuple1)
tuple2=tuple1+tuple(list1)

print(list2)
print(tuple2)
