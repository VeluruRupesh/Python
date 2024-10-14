# Write a program to maximum frequency character in the string

str1=input("Enter any string: ")
str2=str()

for ch in str1:
    if ch not in str2:
        str2=str2+ch
print(str1)
print(str2)

list1=[]
for ch in str2:
    c=str1.count(ch)
    list1.append([c,ch])
print(list1)    
print(max(list1))    
    
