# Write a program to find maximum and minimum K elements of the tuple
#input: test_tup=(3,7,1,18,9),k=2
#output: (3,1,9,18)
#input: test_tup=(3,7,1),k=1
#output:(1,7)

test_tup=(3,7,1,9,18)
test_tup1=sorted(test_tup)
print(test_tup)
print(test_tup1)
test_tup1=tuple(sorted(test_tup)) # converting list to tuple
print(test_tup1)
k=2
min_value=test_tup1[:k] # start=0 stop=2
max_value=test_tup1[-k:] # start=-2 stop=len(tuple) i.e(-2 and -1), step=1
print(f'min_value is: {min_value}')
print(f'max_value is: {max_value}')
