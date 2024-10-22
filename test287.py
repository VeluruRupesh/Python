# Generator expression example or use case

a=(value for value in range(1,11))
print(a)

for x in a:
    print(x,end=' ')   
print()    
even=(value for value in range(1,21) if value%2==0)
print(even)
for x in even:
    print(x,end=' ')
