# Accept the number of terms say n from the user and displax the dictionary in the
# form of {n:n*5} for example:
# If number of terms entered by user is 4 then the expected dictionarx is
#{1:5,2:10,3:15,4:20}

n=int(input("Enter any number: "))
dict1={}
for i in range(1,n+1):
    dict1[i]=i*5
print(dict1)    
