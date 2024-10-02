#Write a program to input Name,subject1,sub2,sub3 and caluculate total marks,
#avg marks

#Input
Name = input("Enter Student Name: ")
sub1 = float(input("Enter Subject1 Marks: "))
sub2 = float(input("Enter Subjecct2 Marks: "))
sub3 = float(input("Enter Subject3 Marks: "))

#Process
total = sub1+sub2+sub3
avg = total/3

#Output
print("Student Name: ",Name)
print("Subject1 Marks: ",sub1)
print("Subject2 Marks: ",sub2)
print("Subject3 Marks: ",sub3)
print("Total Marks: ",total)
print("Average Marks: ",round(avg,2))
