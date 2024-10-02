#New style string formatting
rollno=101
name="Rupesh"
course="Python"
fee=5000.0
print("""Rollno={}
Name={}
Course={}
Fee={}""".format(rollno,name,course,fee))

print("""Rollno={:d}
Name={:s}
Course={:s}
Fee={:.2f}""".format(rollno,name,course,fee))

print("""Decimal Integer={}
Octal Integer={:o}
Hexa Decimal Integer={:x}
Binary Integer={:b}""".format(10,10,10,10))


print("""Float in Fixed={:.2f}
Float in Exponent={:e}""".format(1.5,1.5e-2))

print("""String is={:s}
charater is={:c}""".format("Rupesh",70))
