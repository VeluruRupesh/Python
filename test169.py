# Write a program to create list of tuple from given list jhaving number and it's
#cube in the each tuple
#Input: list=[1,2,3]
#output: [(1,1),(2,8),(3,27)]

list1=[1,2,3,4,5]
list2=[(n,n**3) for n in list1]
print(list1)
print(list2)
