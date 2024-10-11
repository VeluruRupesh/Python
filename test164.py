# Wrirwe a program to read 3x3 matrix and display
matrix1=[[int(input()) for j in range(3)] for i in range(3)]
print(matrix1)
matrix2=[[int(input()) for j in range(3)] for i in range(3)]
print(matrix2)         
matrix3=[[matrix1[i][j]+matrix2[i][j] for j in range(3)] for i in range(3)]
print(matrix3)
