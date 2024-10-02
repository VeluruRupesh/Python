# Write  program to find input password is valid or invalid

pwd=input("Enter Password: ")#abcd12$%
ac,dc,sc=0,0,0
for ch in pwd:
    if (ch>="A" and ch<="Z") or (ch>="a" and ch<="z"):
        ac+=1
    elif ch>='0' and ch<='9':
        dc+=1
    else:
        sc+=1
if (ac+dc+sc)>=8:
    if ac==4 and dc==2 and sc>=2:
        print("Password is valid")
    else:
        print("Password is invalid, password must have 4 alphabets 2 digits 2 special charac   ters")
else:
    print("Lenght of password must be greater than or equal to 8")
            
