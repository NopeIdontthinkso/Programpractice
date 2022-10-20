from turtle import width
from pycat_turtle import Turtle
from pycat.core import Window, Point, Sprite
from random import randint


w = Window()
t = w.create_sprite(Turtle)


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height =  height

    def draw(self, x1, y1):
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


class RobotPart:

    def __init__(self, x, y, width, height):
        r = Rect(width, height)
        r.draw(x, y)


class Robot:

    def __init__(self, x, y, w, h):
        RobotPart(x, y, w/5, h/5)
        RobotPart(x, y-2*h/5, w/5, 2*h/5)
        RobotPart(x, y-4*h/5, w/15, 2*h/5), RobotPart(x+2*w/15, y-4*h/5, w/15, 2*h/5)
        RobotPart(x-2*w/5, y-h/15, 2*w/5, h/15), RobotPart(x+w/5, y-h/15, 2*w/5, h/15)

        
# b = RobotPart(500, 500, 100, 100)
# c = RobotPart(500, 300, 100, 200)
# d = RobotPart(500, 100, 100/3, 200), RobotPart(500+200/3, 100, 100/3, 200)
# e = RobotPart(300, 500-100/3, 200, 100/3), RobotPart(600, 500-100/3, 200, 100/3)
        
x = 200
y = 300

for i in range(50):
    a = randint(50, 200)
    b = randint(50, 200)
    Robot(x, y, a, b)
    x += a

w.run()