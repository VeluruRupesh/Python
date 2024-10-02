# Write a program to find input number is even or odd

num=int(input("Enter Number: "))
remainder=num%2
result="Even" if remainder==0 else "Odd"
print(result)
