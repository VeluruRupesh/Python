# Write a program to write factorial of input number

num=int(input("Enter any number: "))
fact=1
while num>0:
    fact=fact*num
    num=num-1
    #break
else:
    print(f"Factorial is {fact}")
