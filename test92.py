# Write a program to input 10 numbers and print sum,avg
s=0
i=1
while i <=10:
    num=int(input("Enter Any Number: "))
    s+=num
    i=i+1

avg=s/10
print(f"Sum is {s}")
print(f"Avg is {avg}")
