dict1={1:'One',
       2:'Two',
       3:'Three'}
for x in dict1:
    print(x,dict1[x])
print()
courses={'python':4000,'java':2000,'oracle':4000}
for cname in courses:
    print(cname,courses[cname])
print()
sales={2010:56000,2011:25000,2012:58000,2013:780000}
s=0
for year in sales:
    print(f'{year} --> {sales[year]}')
    s=s+sales[year]

print(f'Total sales is: {s}')
