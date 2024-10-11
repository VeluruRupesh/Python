# In given list of values count +ve,-ve and zeros

list1=[5,8,9,1,-3,-6,-10,-5,9,-3,-0,1,4,0,7,-9,-12]
pc,nc,zc=0,0,0
for i in range(len(list1)): #start=0,stop=17,step=1 -->0 1 2 3 4 5 ..17
    if list1[i]>0:
        pc+=1
    elif list1[i]<0:
        nc+=1
    else:
        zc+=1
print(f'Count of List1 is: {list1}')
print(f'Positive count is: {pc}')
print(f'Negetive count is: {nc}')
print(f'Zero count is: {zc}')
