from pycat_turtle import Turtle
from pycat.core import Window, Point, Sprite

w = Window()


t = w.create_sprite(Turtle, x= w.width/2, y= w.height/2)


t.draw_star(20, 100)
w.run()