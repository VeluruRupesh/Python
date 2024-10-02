import math
print("*****MENU*****")
print("1. Find Area of Curcle")
print("2. Find the Aras of Triangle")
print("3. Exit")
opt=int(input("Enter your Optuon: "))
match(opt):
    case 1:
        r=float(input("Enter Radius Value: "))
        a=math.pi*r*r
        print(f"Area of the Circle is: {a:.2f}")
    case 2:
        base=float(input("Enter base of the Triangle: "))
        height=float(input("Enter height of the Triangle: "))
        a = 0.5*base*height
        print(f"Area of the the Triangle is {a:.2f}")
    case 3:
        print("Bye")
    case _:
        print("Invalid Option. Please ty again..")
