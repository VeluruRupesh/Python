# Write a program to check if the string contains any special character.

#input: Geeks$For$Geeks
#Output: String is not accepted.
#input: Geeks For Geeks
#Output: String is  accepted.

#str1='Geeks$For$Geeks'
str1=input("Enter any string: ")
sp="$§@%*°^°!"
found=False
for ch in str1:
    if ch in sp:
        found=True
        break
if found:
    print("String is not accepted.")
else:
    print("String is  accepted.")
