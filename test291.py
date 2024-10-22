def calculator(n1,n2,calc):
    result=calc(n1,n2)
    return result


res1=calculator(10,5,lambda a,b:a+b)
res2=calculator(5,2,lambda a,b:a*b)
res3=calculator(20,55,lambda a,b:a/b)
print(res1,res2,res3,sep='\n')
    
