# Write s program to add two matrices

matrix1=[[1,2],[3,4]]
matrix2=[[5,6],[7,8]]
matrix3=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(matrix1[i][j]+matrix2[i][j])
    matrix3.append(row)    
print(matrix1)
print(matrix2)
print(matrix3)
