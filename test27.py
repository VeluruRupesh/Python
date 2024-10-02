#Write a program for swaping two integers

a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
print("Before Swaping : ",a,b)
#Method-1
c=a
a=b
b=c
print("After Swaping : ",a,b)

#Method-2
a=a+b
b=a-b
a=a-b
print("After Swaping : ",a,b)

#Method-3

a,b=b,a
print("After Swaping : ",a,b)

