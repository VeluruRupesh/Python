# use cases to test if..elif..elif..else

if True:
    print("A")
elif True:
    print("B")
elif True:
    print("C")

if False:
    print("a")
elif True:
    print("b")
elif True:
    print("c")

if False:
    print("a")
elif False:
    print("b")
elif True:
    print("c")

if False:
    print("A")
elif False:
    print("B")
elif False:
    print("C")
else:
    print("D")
