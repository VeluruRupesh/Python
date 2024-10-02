#Write a program to find simple interest
#input
#Amount
#Time
#Rate
#si =PTR/100

amt = float(input("Enter Amount :$"))
time=int(input("Enter Time: "))
rate= float(input("Enter rate of Interest:$"))
si =(amt*time*rate/100)
print("Simple Interest:$",si)
