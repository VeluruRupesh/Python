# Write a program to reverse number
# input 123
# output 321

# Method 1 without using while

num= input("Enter any Number: ")
rev_num=num[::-1]
print(num)
print(rev_num)

# Method-2 with while loo

num=int(input("Enter any number: "))

rev=0
while num>0:
    r=num%10
    rev=(rev*10)+r
    num=num//10
print(rev)    
    
