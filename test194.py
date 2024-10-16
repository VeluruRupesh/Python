# Find words which are greater than given length K
# Input: str= "hello geeks for geeks is computer science portal"
# k=4
#Ouput: hello geeks geeks computer science portal

str1=input("Enter any string: ")
list1=str1.split()
print(list1)
k= int(input("Enter value of K: "))
for word in list1:
    if len(word) > k:
        print(word,end=' ')

