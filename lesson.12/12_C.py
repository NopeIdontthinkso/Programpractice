from pycat.core import Window,Sprite,Color
from random import randint

w=Window(1200,800)

class Square(Sprite):

    def on_create(self):
        self.scale = 10
        self.goto_random_position()
        self.rotation = randint(0,360)
        self.x_speed = randint(2,10)
        self.y_speed = randint(2,10)
        self.add_tag('p')


    def on_update(self, dt):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > w.width or self.x < 0:
            self.x_speed =- self.x_speed
        if self.y > w.height or self.y < 0:
            self.y_speed =- self.y_speed

class Button(Sprite):
    def on_create(self):
        self.scale = 100
        self.y = 100
    def on_left_click(self):
        particles = w.get_sprites_with_tag('p')
        if self.color == Color.RED:
            for p in particles:
                p.delete()
        if self.color == Color.GREEN:
            for i in range(10):
                w.create_sprite(Square)


        
w.create_sprite(Button , x=100 , color=Color.GREEN)
w.create_sprite(Button , x=400 , color=Color.RED)
w.run()