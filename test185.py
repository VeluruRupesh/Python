# write a program to Reverse words in a given string
# input: str="geeks quiz practice code"
#output: str= code practice quiz geeks

str1="geeks quitz practice code"
list1=str1.split()
print(list1)
list1=list1[::-1]
print(list1)
str2=' '.join(list1)
print(str2)
