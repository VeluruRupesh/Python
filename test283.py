def fun1(): # Normal Function
    return 10 # function returns value and terminates here
    return 20
    return 30
    return 40

def fun2(): # Generator Function
    yield 10 # function yield key word passes  value and resumes from nex value
    yield 20
    yield 30
    yield 40


res1=fun1()
print(res1)
res2=fun2()
print(res2)
for value in res2:
    print(value)
