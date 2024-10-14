# Write a program to print even length words in a string
#input: s="This is a python language"
#output: This is pythib language
# here a is odd as it has one letter

s="This is a python language"
list1=s.split()
print(list1)
for word in list1:
    if len(word)%2==0:
        print(word,end=' ')
