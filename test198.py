# Write a program to execute N commaands and those commands should be pop(),remove() and discard()

n=int(input())
A=set(map(int,input().split()))
N=int(input())
for i in range(N):
    cmd=input().split() # ex: remove 5
    if cmd[0]=="remove":
        A.remove(int(cmd[1]))
    elif cmd[0]=="discard":
        A.discard(int(cmd[1]))
    elif cmd[0]=="pop":
        A.pop()
print(sum(A))        
