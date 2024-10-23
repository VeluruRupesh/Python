def print_numbers(n):
    if n>1:
        print_numbers(n-1) # recursion call
    print(n)        


print_numbers(5)
print('*********************')
print_numbers(10)

print('*********************')
def display_numbers(n):
    if n<5:
        display_numbers(n+1)
    print(n)

display_numbers(1)    

