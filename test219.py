# Write a program to read sales of n sales persons and display
# each sales person is having name and sales

n= int(input("Enter how many sales person: "))
#Without dictionary comprehension
sales={}
for i in range(n):
    name=input("Enter Name of the sales person: ")
    s=float(input("Enter Sales: "))
    sales[name]=s

print(sales)    

#With Dictionary Comprehension

sales = {input("Enter Name: "):float(input("Enter Sales: ")) for i in range(n)}
print(sales)
         
