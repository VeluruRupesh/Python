# Find maximum of any number of values

def maximum(*values):

    if len(values)==0:
        return None
    else:
        m=values[0]
        for i in range(1,len(values)):
            if values[i]>m:
                m=values[i]
        return m        


res1=maximum()
print(res1)
    
res2=maximum(10,20)
print(res2)
res3=maximum(10,50,70,20,90,40,50)
print(res3)
