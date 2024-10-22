students_dict={'Rupesh':'A',
               'Suresh':'B',
               'Harish':'C',
               'Arun':'B',
               'Vijay':'A'}

s1=filter(lambda a:a[1]=='A',students_dict.items())
for value in s1:
    print(value)

s2=filter(lambda a:a[1]=='B',students_dict.items())
for value in s2:
    print(value)
s3=filter(lambda a:a[1]=='C',students_dict.items())
for value in s3:
    print(value)
