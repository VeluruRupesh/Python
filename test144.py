# Write a program to read name, n subject marks caluculate total and avg marks

name=input("Enter Name of the student: ")
n= int(input("How many subjects? "))
marks=[]
for i in range(n):
    s=int(input("Enter Marks: "))
    marks.append(s)

total=sum(marks)
avg=total/n
print(f"Name: {name}")
print(f'Marks: {marks}')
print(f'Total Marks: {total}')
print(f'Average of Marks: {avg:.2f}')
    
