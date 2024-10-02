# Write a program to check input number is palindrom or not?
# number is equal to reverse number is palindrom (ex:121-121)

num= int(input("Enter any Number: "))
temp=num
rev=0
while num>0:
    r=num%10
    rev=(rev*10)+r
    num=num//10

if rev==temp:
    print(f'{temp} is a Palindrom')
else:
    print(f'{temp} is not a Palindrom')

