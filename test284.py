#Generator example or use case

def even_generator():
    for num in range(1,50):
        if num%2==0:
            yield num


even=even_generator()
print(even)
value1=next(even)
value2=next(even)
value3=next(even)
print(value1,value2,value3,end=' ')

for value in even:
    print(value,end=' ')
