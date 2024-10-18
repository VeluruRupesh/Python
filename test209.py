grade_dict={'Rupesh':'A',
            'Suresh':'B',
            'Vijay':'A',
            'Arun':'C',
            'Kiran':'B'}
acount=0
bcount=0
ccount=0
items_view=grade_dict.items()

for stud in items_view:
    name,grade=stud
    print(f'{name}-->{grade}')
    if grade=='A':
       acount+=1
    elif grade=='B':
        bcount+=1
    elif grade=='C':
        ccount+=1
print(f'A Grade count: {acount}')
print(f'B Grade count: {bcount}')
print(f'C Grade count: {ccount}')
