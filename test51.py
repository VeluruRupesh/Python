# Write a program to find area of Triangle
# Input
#Base
#Height
#area=0.5*b:h

b=float(input("Enter base of the Triangle: "))
h=float(input("Enter height of the Triangle: "))
area=0.5*b*h
print("Area of Triangle with base={:.2f} and height={:.2f} is {:.2f}".format(b,h,area))
