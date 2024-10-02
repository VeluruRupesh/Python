#example of converting string to integer, integer values are given in
#different formats

a=int("45")
b=int("0o12",base=8)
c=int("0xab",base=16)
d=int("0b101",base=2)
print(a,b,c,d)
print(a,oct(b),hex(c),bin(d))
