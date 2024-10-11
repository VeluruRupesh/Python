list1=list(range(10,110,10))
print(list1)
list2=list1[::] # stat=0,stop=10,step=1 -->0 1 2 3 4 5 6 7 8 9
print(list2)

list3=list1[:] # stat=0,stop=10,step=1 -->0 1 2 3 4 5 6 7 8 9
print(list3)
