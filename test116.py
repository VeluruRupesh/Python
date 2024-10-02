# Wrire a program to display all the number which are divisible by 11 and no divisible by 2 between 100 and 500

for num in range(100,501):
    if num%11==0 and num%2!=0:
        print(num)
