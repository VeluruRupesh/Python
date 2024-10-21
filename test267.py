def add(*vargs,**kwargs):
  s=0
  if len(vargs)>0:
      for value in vargs:
          s+=value
  if len(kwargs)>0:
      for value in kwargs.values():
          s+=value
  return s

res1=add(10,20)
print(res1)
res2=add(a=10,b=20)
print(res2)
res3=add(10,20,a=200,b=550)
print(res3)
