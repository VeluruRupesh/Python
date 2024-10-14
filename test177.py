#Counting number of matching characters in the pair of strings
str1=input("Enter first string: ")
str2=input("Enter second string: ")
set1=set(str1)
set2=set(str2)
set3=set1.intersection(set2)
print(set3)
