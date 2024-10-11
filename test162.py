# Wrire a program to read marks of M students and each student has N subjects
M=int(input("Enter how many Students: "))
N=int(input("Enter how many subjects: "))
marks=[]
for i in range(M):
    r=[]
    for j in range(N):
        s=int(input("Enter Marks: "))
        r.append(s)
    marks.append(r)
print(marks)

for i in range(M):
    total=sum(marks[i])
    average=total/N
    result="Pass"
    for j in range(N):
        if marks[i][j]<40:
            result="Fail"
            break
    print(marks[i],total,average,result)
    
