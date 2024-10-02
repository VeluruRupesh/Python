# Write a program to find input number is argmstrong number or not
#sum of digits to the power of the lenght of the number
#example: 153-->1**3+5**3+3**3 -->1+125+27=153

num=int(input("Enter any number: "))
temp=num
s=0
while num>0:
    r=num%10
    s=s+(r**3)
    num=num//10
if s==temp:
    print('Armstrong Number')
else:
    print('Not Armstrong number')     
