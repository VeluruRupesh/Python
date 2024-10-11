list1=[10,20,30,40,50]
print(list1[0],list1[1],list1[2],list1[3],list1[4])
print(list1[-1],list1[-2],list1[-3],list1[-4],list1[-5])

for i in range(5): #start=0,stop=5,step=1 -->0 1 2 3 4
    print(list1[i],end=' ')
print()
for i in range(-1,-6,-1): #start=-1,stop =-6 step=-1 -->-1 -2 -3 -4 -5
    print(list1[i],end=' ')

print()
#Output

for i in range(0,5,2):
    print(list1[i],end=' ')
print()
for i in range(len(list1)): #start=0,stop=5,step=1
    print(list1[i],end=' ')
