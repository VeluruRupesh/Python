def calculator(opr):
    def calc(num1,num2):
        match(opr):
            case'+':
                return num1+num2
            case'-':
                return num1-num2
            case'*':
                return num1*num2
            case'/':
                return num1/num2
            case _:
                return None
    return calc

calc_add=calculator('+')
calc_sub=calculator('-')
calc_mul=calculator('*')
calc_div=calculator('/')

res1=calc_add(100,200)
res2=calc_sub(800,900)
res3=calc_mul(200,250)
res4=calc_div(3,9)
print(res1,res2,res3,res4,sep='\n')        
