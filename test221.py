# Create even numbers square dictionary

dict1={num:num**2 for num in range(1,21) if num%2==0}
print(dict1)

dict2 ={num:num**2 for num in range(2,21) if num%2!=0}
print(dict2)
