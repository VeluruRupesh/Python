# Given an array of A of positive integers. Your task is to find the leaders
# in the array. An element of array is a leader if it is greater than or equal
# to all the elements to its right side. The rightmost elements is always a
# leader
# Example:
#Input -> n=6 A=[16,17,4,3,5,2]
#Output: 17 5 2
n=6
A=[16,17,4,3,5,2]
for i in range(len(A)): #start=0,stop=6 ,step=1 --> 0 1 2 3 4 5
    ans=True
    for j in range(i+1,len(A)): # start =1 ,stop=6 ,step=1 -->1 2 3 4 5
        if A[i]>A[j]:
            leader=A[i]
            
        else:
            ans=False
            break
        
    if ans==True:
        print(leader)
      
print(A[i])
