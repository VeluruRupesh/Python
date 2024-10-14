# Write a prograam to to check if the ggiven string is palindrom or not
#str1=madam
#rev=madem
#reverse is dsame as original string and it is called as palindrom
str1=input("Enter any string: ")
str2=str1[::-1] # start-1,stop =-6,step=-1

if str1==str2:
    print(f"String is Palindrom")
else:
    print(f"String is not a palindorm")
print(str1,str2)    
