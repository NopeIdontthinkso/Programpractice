from turtle import width
from pycat_turtle import Turtle
from pycat.core import Window, Point, Sprite

w = Window()

t = w.create_sprite(Turtle, x= w.width/2, y= w.height/2)


class Rect:
    def __init__(self ,width ,height):
        self.width = width
        self.height =  height

    def draw(self ,x1 ,y1):
        t.x = x1
        t.y = y1
        t.rotation = 0
        t.draw_forward(self.width)
        t.rotation += 90 
        t.draw_forward(self.height)
        t.rotation += 90
        t.draw_forward(self.width)
        t.rotation += 90 
        t.draw_forward(self.height)


r = Rect(100,200)

for i in range(10):    
    r.draw(i*100,i*100)
w.run()