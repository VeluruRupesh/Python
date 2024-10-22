def draw(ch):

    def draw_line(s):
        for i in range(s):
            print(ch,end='')
        print()
    return draw_line

draw_stars=draw('*')
draw_dollar=draw('$')
draw_line=draw('-')

draw_dollar(10)
draw_stars(10)
draw_line(10)
draw_stars(50)
