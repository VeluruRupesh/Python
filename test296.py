list1=[1,2,3,4,5]
list2=[10,20,30,40,50]

a= map(lambda a,b:a+b,list1,list2)
list3=list(a)
print(list1,list2,list3,sep='\n')
