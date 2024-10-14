names_list=['Rupesh',
           'Rajesh',
           'Arun',
           'Narayana',
           'Krishna',
           'Suresh',
           'Nagendra']
for name in names_list:
    if name.endswith("a"):
        print(name)
print("*************************")
for name in names_list:
    if name.endswith(("a","n")):
        print(name)


print('**************************')
for name in names_list:
    if name.endswith(('h','e','n')):
        print(name)

