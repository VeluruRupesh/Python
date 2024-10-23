# Find sum of digits of input number using recursion

def sum_digits(num):
    if num==0:
        return 0
    else:
        return num%10+sum_digits(num//10)


number=int(input("Enter any number: "))
res=sum_digits(number)
print(res)
