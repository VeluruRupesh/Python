# Wrire a program to read the sales of M sales persons N sales
M=int(input("Enter How many sales persons: "))
N= int(input("Enter how many sales: "))

sales=[]
for i in range(M):
    row=[]
    for j in range(N):
        s=int(input("Enter Sales: "))
        row.append(s)
    sales.append(row)
print(sales)        
