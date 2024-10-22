def find_power(num):
    def power(p):
        r=num**p
        return r
    return power

p5=find_power(5)
p9=find_power(9)
print('**Power of 5***')
print()
res1=p5(1)
res2=p5(2)
print(res1,res2,end='')
print()
print('**Power of 9***')
print()
res3=p9(2)
res4=p9(3)
print(res3,res4,end='')
