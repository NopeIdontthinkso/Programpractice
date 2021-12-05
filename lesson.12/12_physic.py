import random
from pycat.core import Window
from pycat.core import Sprite
from random import randint

w=Window(1200,800)

class Square(Sprite):

    def on_create(self):
        self.scale = 10
        self.goto_random_position()
        self.rotation = randint(0,360)
        self.x_speed = randint(2,10)
        self.y_speed = randint(2,10)


    def on_update(self, dt):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > w.width or self.x < 0:
            self.x_speed =- self.x_speed
        if self.y > w.height or self.y < 0:
            self.y_speed =- self.y_speed

        
for i in range(100):
    w.create_sprite(Square)

w.run()