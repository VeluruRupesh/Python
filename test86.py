# Write a program to find max of 3 numbers without using AND operator

a=int(input("First Number: "))
b= int(input("Second Number: "))
c= int(input("Thrid Number: "))

if a>b:
    if a>c:
        print(f"{a} is max")
    else:
         print(f"{c} is max")
elif b>a:
    if b>c:
        print(f"{b} is max")
    else:
        print(f"{c} is max")
elif c>a:
    if c>b:
        print(f"{c} is max")
    else:
        print(f"{b} is max")
        
