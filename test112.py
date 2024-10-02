# Write a program to print sum of n numbers, input n numbers from keyword
n=int(input("Enter how many numbers: ")) #4
s=0
for i in range(n): #start=0,stop=4 step =1
    num=int(input("Enter any number: "))
    s+=num
print(f"Sum is {s}")    
    
            
