# Write a program to find input string is alphabhetic or not without using isalpha() method

str1=input("Input Enter Any String: ")
result=True
for ch in str1:
    if (ch>="A" and ch<="Z") or (ch>="a" and ch<="z"):
        pass
    else:
        result=False
        break
print(result)    
