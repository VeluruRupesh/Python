r1=range(1,50,2)
for value in r1:
    print(value,end=' ')

def float_range(start,stop,step):
    if start<stop:
        while start<stop:
            yield start
            start=start+step
    elif start>stop:
        while start>stop:
            yield start
            start=start+step
print()
r2=float_range(1.0,10.0,1.0)
for value in r2:
    print(value,end=' ')
print()

r3=float_range(10.0,1.0,-1.0)
for value in r3:
    print(value,end=' ')
