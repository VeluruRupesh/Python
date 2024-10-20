def add(a,b):
    c=a+b
    print(f'Sum of {a} and {b} is : {c}')
    
add(100,200)
add(1.5,1.2)
add(1+2j,1+3j)
add('A','B')


def add1(a:int,b:int): # here int is hint of data type ( Funtion type hint)
    c=a+b
    print(f'Sum of {a} and {b} is : {c}')

add1(100,200)
add1(1.5,2.5)
add1(1+2j,3+4j)
