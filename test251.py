def draw_line1(ch):
    print(ch*20)


draw_line1("*")
draw_line1('$')

print('###############################')
def draw_line2(ch,len):
    print(ch,len)

draw_line2('*',12)
draw_line2('$',20)
draw_line2('%',5)
print('###############################')
def draw_line(ch,len=20):
    print(ch*len)

draw_line('*')
draw_line('$',40)
