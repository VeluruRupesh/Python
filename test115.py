# Write a program to find sum of even and odd numbers between 12 and 37 both are included

es=0
os=0
for num in range(12,38): #start=12 stp=38 step=1
    if num%2==0:
        print(f'Even {num}')
        es=es+num
    else:
        print(f'Odd {num}')
        os=os+num

        
print(f'Even Number sum is {es}')
print(f'Odd Number sum is {os}')
