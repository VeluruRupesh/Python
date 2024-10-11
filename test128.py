list1=list(range(10,110,10))
print(list1)
list2=list1[::1] #start=0,stop=10,step=1 -->0 1 2 3 4 5 6 7 8 9
print(list2)
list3=list1[::2] #start=0,stop=10,step=2 -->0 2 4 6 8
print(list3)
list4=list1[::-1]# start=-1,stop=-11 step=-1
print(list4)
list5= list1[::-2] # start -1, stop=-11 step=-2
print(list5)
