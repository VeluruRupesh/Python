# You are given a set A and N number of other sets. These N number of sets have to perfrom
# some specific mutation operations on set A
#Your task is to execute those operations and print the sum of elements from set A.
# example:
# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66
# output: 38

n=int(input())
A=set(map(int,input().split()))
N=int(input()) # number of operations
for i in range(N):
    cmd=input().split()
    B=set(map(int,input().split()))
    if cmd[0]=="update":
        A.update(B)
    if cmd[0]=="difference_update":
        A.difference_update(B)
    if cmd[0]=="intersection_update":
        A.intersection_update(B)
    if cmd[0]=="symmetric_difference_update":
        A.symmetric_difference_update(B)
print(sum(A))        
