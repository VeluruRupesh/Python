# Write a program accept the key from the user and remove that key from the dictionary if it is present.

d1={1:10,2:20,3:30,4:40,5:50}
k = int(input("Enter the key: "))
if k in d1:
    del d1[k]
else:
    print("Key do not exists")
print(d1)    
