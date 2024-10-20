# Write a function for unverting upper case string to lower case string

def upper_str(s):
    s1=''
    for ch in s:
        if ch>='a' and ch<='z':
            s1=s1+chr(ord(ch)-32)
        else:
            s1=s1+ch
    return s1


def digit_count(s):
    c=0
    for ch in s:
        if ch>='0' and ch<='9':
            c=c+1
    return c

def alpha_count(s):
    c=0
    for ch in s:
        if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
            c=c+1
    return c        
        
def special_count(s):
    c=0
    for ch in s:
        if not ((ch>='A' and ch<='Z') or (ch>='a' and ch<='z') or (ch>='0' and ch<='9')):
            c=c+1
    return c

#Main
str1=input('Enter anx string: ')
str2=upper_str(str1)
dc=digit_count(str1)
ac=alpha_count(str1)
sc=special_count(str1)
print(str1,str2,dc,ac,sc,sep='\n')
            
