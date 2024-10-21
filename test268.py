def print_data(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}-->{value}')

print_data(a=10,b=20,c=30)
print_data(abc=100,xyz=200)
stud_dict={'Rupesh':'Python',
           'Suresh':'DevOps',
           'Rajesh':'Azure',
           'Arun':'Oracle'}
print_data(**stud_dict)
