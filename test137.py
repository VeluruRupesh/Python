# Write a program to find missing number in the array with distinct integers in the rage of 1 to N
#ex:
#input:
#N=10
#A=[6,1,2,8,3,4,7,10,5]
#Output=9
N=10
A=[6,1,2,8,3,4,7,10,5]
for val in range(1,N+1): #1 2 3 4 5 6 7 8 9 10
    if val not in A:
        missing_value=val
        break
print(A)
print(missing_value)
    

