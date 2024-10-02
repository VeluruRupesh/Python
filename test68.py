a=100
print(id(a),a)
a=200
print(id(a),a)

#id changed due to immutable or sclar objects

f1=1.5
print(id(f1),f1)
f1=1.2
print(id(f1),f1)

#here address i.e a ,b,c,d address is shared and 100 memory is reserved only
#one time and it increases the sapace and efficiency as immutables are sharable.
a=100
b=100
c=100
d=100

print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))

