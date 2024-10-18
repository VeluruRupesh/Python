#1 2 3 4 5
#  2 3 4 5
#    3 4 5
#      4 5
#        5

for r in range (1,6):
    for c in range(1,6):
        if c>=r:
            print(c,end=' ')
        else:
            print(' ',end=' ')
    print()       
