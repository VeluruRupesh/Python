list1=list(range(10,110,10))
print(list1)

list2=list1[0:10] #start=0 stop=10 step=1 -->0 1 2 3 4 5 6 7 8 9
print(list2)

list3 =list1[0:5] #start = 0 ,stop =5 step =1
print(list3)

list4=list1[4:9] #start=4,stop=9 step=1
print(list4)

list5=list1[-5:-9] #start=-5,stop=-9,step=1
print(list5) # here start is less than stop so it give empty list

list6 =list1[-9:-5] #start=-9,stop=-5 ,step=1
print(list6)

list7=list1[1:-1] #start=1,stop=-1 or stop=9,step=1
print(list7)

list8=list1[3:-3] # start =3 stop=7 or -3 step=1
print(list8)
