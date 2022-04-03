from pycat.core import Window, Point
from random import randint

w = Window()

def get_random_point():
    x = randint(0, w.width)
    y = randint(0, w.height)
    return Point(x, y)

def draw_triangle(a:Point, b:Point, c:Point, line_width:int = 1):
    w.create_line(a.x, a.y, b.x, b.y, line_width)
    w.create_line(b.x, b.y, c.x, c.y, line_width)
    w.create_line(c.x, c.y, a.x, a.y, line_width)

def draw_many_triangle(a:Point, b:Point, c:Point, line_width:int = 1, time:int = 1):
    if time <=0:
        draw_triangle(a, b ,c, line_width)
        return
    else:
        d = (a+b)/2
        e = (b+c)/2
        f = (c+a)/2
        time -= 1 
        draw_many_triangle(d ,e ,f , line_width ,time )
        draw_many_triangle(a ,d ,f , line_width ,time )
        draw_many_triangle(d ,e ,b , line_width ,time )
        draw_many_triangle(c ,e ,f , line_width ,time )

def draw_random_triangle(line_width: int = 1):
    a = get_random_point()
    b = get_random_point()
    c = get_random_point()
    draw_triangle(a, b ,c, line_width)


draw_many_triangle(a=get_random_point(), b=get_random_point(), c=get_random_point() ,line_width = 1, time= 6)

w.run()
