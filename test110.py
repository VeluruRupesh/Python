# Write a program to generate mathematical table with input number
# Number 5
#5x1=5 ... 5x10=50

num=int(input("Enter any number: "))

for i in range(1,11): #start 1 stop 11 step 1 -->1 2 3 4 5 6 7 8 9 10
    pr=num*i
    print(f'{num}x{i}={pr}')
