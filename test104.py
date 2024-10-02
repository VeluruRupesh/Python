#Name Validation--> Name should be in BLOCK letters
name=input("Enter any name: ")
ac=0
for ch in name:
    if ch>="A" and ch<="Z":
        pass
    else:
        ac+=1

if ac==0:
    print("Name is Valid.")
else:
    print("Name is invalid.")
    
