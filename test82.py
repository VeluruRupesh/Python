# Write a program to accept the cost price of the bile and display the road tax according to criteria
# Cost price (In Rs)           Tax
# >10000                    15%
#>50000 and <=1000000       10%
#<=50000                    5%

cp=int(input("Enter cost price of the bike(Rs.): "))
if cp >100000:
    tax=cp*15/100
elif cp>50000 and cp<=100000:
    tax= cp*(10/100)
else:
    tax=cp*(5/100)

print(f'Bike Price is Rs {cp:.2f}')
print(f'Total Tax of Bike is Rs {tax:.2f}')
