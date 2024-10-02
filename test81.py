# Write a program to calaculate the EB ,accept eh number of units fromthe user
#according to criteria:
#     Unit                Price
# First 100 Units       No Charge
#Next 100 units         Rs 3 per unit
# After 200 Units       rs 10 per uinit
# For example if input unit is 350 then total bill amount is Rs2000)

units= int(input("Enter number of units: "))
if units<=100:
    amt=0
    print("For {units} ther is No Charge on your EB")
elif units >100 and units <=200:
    amt=(units-100)*5
    print(f'your EB bill for {units} is Rs.{amt:.2f}')
else:
    amt=500+(units-200)*10
    print(f'your EB bill for {units} is Rs.{amt:.2f}')
    
