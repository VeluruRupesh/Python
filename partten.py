#5
#5 4
#5 4 3
#5 4 3 2
#5 4 3 2 1

for r in range(5,0,-1):
    for c in range(5,0,-1):
        if c>=r:
            print(c,end='')
    print()    
