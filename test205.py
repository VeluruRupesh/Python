A={frozenset(range(10,60,10)),frozenset(range(60,110,10))}
print(A)

for s in A:
    print(s)
print()
for s in A:
    for value in s:
        print(value,end=' ')
    
