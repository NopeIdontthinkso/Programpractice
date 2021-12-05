from ctypes import set_last_error
from pycat.core import Window,Sprite,Color
from random import randint, random

w=Window(1200,800)

class Square(Sprite):

    def on_create(self):
        self.time = 0
        self.life_time = 0.2 + random()/2
        


    def on_update(self, dt):
        self.time += dt
        if self.time > self.life_time:
            self.delete()

class Firework1(Square):
    def on_create(self):
        super().on_create()
        self.scale = 10
        self.y = 0
        self.x = w.width/2
        self.rotation = randint(70,110)
    def on_update(self, dt):
        super().on_update(dt)
        self.move_forward(10)
        if self.time > self.life_time:
            for i in range(20):
                w.create_sprite(Firework2 , x=self.x , y=self.y)
        

class Firework2(Square):

    def on_create(self):
        super().on_create()
        self.scale = 5
        self.rotation = randint(0,360)
    
    def on_update(self, dt):
        self.move_forward(5)
        super().on_update(dt)

        



        

class Button(Sprite):
    def on_create(self):
        self.scale = 100
        self.y = 100
    def on_left_click(self):
        for i in range(5):
            w.create_sprite(Firework1)


        
w.create_sprite(Button , x=100 , color=Color.BLUE)
w.create_sprite(Button , x=400 , color=Color.RED)
w.run()