# Write a program to count the matching characters in a pair of string
# input: str1='abcdef'
#       str2='defghia'
#output: 4
#(i.e., matching characters: a,d,e,f

str1= input("Enter first string: ")
str2= input("Enter second string: ")
str3=str()
for ch in str1:
    if ch not in str3:
        str3=str3+ch
for ch in str3:
    c=str2.count(ch)
    if c>0:
        print(ch,end='')
