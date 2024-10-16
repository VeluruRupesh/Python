A={1,2,3,4,5}
B={1,2,3,6,7,8}
A.update(B)
print(A)

C={1,2,3,4,5,6}
D={1,2,3,7,8,9}
C.intersection_update(D)
print(C)

E={1,2,3,4,5,6}
F={1,2,3,7,8,9}
E.difference_update(F)
print(E)

G={1,2,3,4,5,6}
H={1,2,3,5,7,8}
G.symmetric_difference_update(H)
print(G)
