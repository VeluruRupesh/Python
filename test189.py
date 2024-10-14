names=['Rupesh',
       'Rajesh',
       'Krishna',
       'Arun',
       'Suresh',
       'Nagendra']
for name in names:
    if name.startswith("R"):
        print(name)

for name in names:
    if name.startswith(('K','N')):
        print(name)
