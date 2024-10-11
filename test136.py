# Write a program for two sum and return position of the number in the list or array
# ex: nums=[2,7,11,15] and target=9

nums=[2,7,11,15]
target=9
for i in range(len(nums)-1):
    if nums[i]+nums[i+1] ==target:
        index_list=[i,i+1]
print(index_list)        
