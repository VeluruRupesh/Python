# Write a program to find factorial of input number
# number 4 -->24 = (1x2x3x4) , Number 3 ---> 6 =(1x2x3)

num=int(input("Enter any number: "))
fact=1
for i in range(1,num+1): # start=1 stop =5 step=1 -->1 2 3 4 5
    fact=fact*i
print(f'factoral of {num} is {fact}')
