sales={2000:45000,
       2001:50000,
       2002:65000,
       2003:74000,
       2004:88000,
       2005:45000,
       2006:90000,
       2007:92000}
for year,s in sales.items():
    print(f'{year}-->{s}')

sales1={year:s for year,s in sales.items() if s<=50000}
print(sales1)
sales2={year:s for year,s in sales.items() if s>50000}
print(sales2)
