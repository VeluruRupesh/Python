# Write a program to find result of a student
# input Name, sub1 ,sub2 Mrarks

name = input("Enter Student Name: ")
sub1 = int(input("Subject1 Marks: "))
sub2= int(input("Subject2 Marks: "))
print(f'{name} is pass') if sub1>=40 and sub2>=40 else print(f'{name} is fail')
