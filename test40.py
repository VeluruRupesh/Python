#Write a program to input lower case character and convert into uppercase char

ch= input("Ener single character (a-z): ")
ch1=chr(ord(ch)-32) #diff b/w upper case and lower case is 32
print(ch,ch1)
