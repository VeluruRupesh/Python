def draw():
    ch="*" #Local Variable
    def drawLine(s):
        for i in range(s):
            print(ch,end='')
        print()
    return drawLine 
    
d=draw()
d(10)
d(20)
d(5)
