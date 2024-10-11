# Wrire a program to create 3x3 matrix and display

matrix1=[]

print("Enter elements of matrix1: ")
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("Enter any value: "))
        row.append(value)

    matrix1.append(row)
print(matrix1)    
