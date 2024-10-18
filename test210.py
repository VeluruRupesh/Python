dict1={1:10,
       2:20,3:30,4:40,5:50}
for a in dict1:
    print(a,dict1[a])

print('****************')
rev_itr=reversed(dict1)
for b in rev_itr:
    print(b,dict1[b])
