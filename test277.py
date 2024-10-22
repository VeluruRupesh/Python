# example of closures or use case of closures

def super_power(num):
    def power(p):
        res=num**p
        return res
    return power

p1=super_power(5)
res1=p1(2)
res2=p1(3)
res3=p1(4)
print(res1,res2,res3,sep='\n')
print('*************************')
def find_power():
    num=5
    def power1(p):
        r=num**p
        return r
    return power1

p1=find_power()
res1=p1(2)
res2=p1(3)

print(res1,res2,end=' ')
