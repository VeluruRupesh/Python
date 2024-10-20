# Write a program to find area of a Triangle
base=0.0 # Global Variable
height = 0.0 # Global Variable

def read():
    global base,height
    base=float(input("Enter Base of the Triangle: "))
    height= float(input("Enter Height of the Triangle: "))
def find_area():
    area=0.5*base*height
    print(f'Area of the Triangle is: {area:.2f}')

read()
find_area()
    
