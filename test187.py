# Write a program to convert snake case to pascal case
# snake case is : a_b_c
#Pascal case is : A ( first lettr is caps)
#input: geeks_for_geeks
#output: GeeksForGeeks

str1="geeks_for_geeks"
list1=str1.split("_")
print(list1)
list1=[s.title() for s in list1]
print(list1)
str2=' '.join(list1)
print(str2)
