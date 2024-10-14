# Wtrie a program to find frequency of eacjh character exisits within string
#input: abcabaababdc
#output: 4a4b2c1d

str1=input("Enter any string: ")
str2=str()
for ch in str1:
    if ch not in str2:
        str2=str2+ch
print(str1)
print(str2)
str3=str()
for ch in str2:
    c=str1.count(ch)
    str3=str3+str(c)+ch
print(str3)    

        
