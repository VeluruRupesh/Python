list1=[4,7,9,1,-4,-8,-3,66,32,12,87,0,12,0,13,-5,-8,0,0]
list2=[value for value in list1 if value>0]
list3=[value for value in list1 if value<0]
list4=[value for value in list1 if value==0]
print(list1,list2,list3,list4,sep='\n')

names=['Rupesh','Rajesh','Arun','Nagendra','Krishna','Suresh','Narayana']
print(names)
names1=[name for name in names if name[-1]=='h']
print(names1)
names2=[name for name in names if name[0]=='R' ]
print(names2)
names3=[name for name in names if name[0]=='R' and name[-1]=='h']
print(names3)
