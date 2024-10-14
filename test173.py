# Write a program to check if the string is symmetrical and palindorm
# or not
#if first half of the string is same and second hald of the string then it is symmetrical
# input: khokho
# input: amaama
# and sting is same if we read forward or backward is palindrom

str1=input("Enter any string: ")
if len(str1)%2==0:
    i=len(str1)//2
    first=str1[:i]
    second=str1[i:]
    if first==second:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
else:
    print("The entered string is not symmetrical")
if str1==str1[::-1]:
    print("The entered string is palindorm")
else:
    print("The entered string is not palindorm")
