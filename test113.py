# Write a program to find input number is prime number or not
# Prime number is divisible by itself or with 1 (ex: 5)

num=int(input("Enter any Number: "))
c=0
for i in range(1,num+1):
    if num%i ==0:
        c+=1

if c==2:
    print("This number is Prime.")
else:
    print("This Number is not a Prime.")
        
