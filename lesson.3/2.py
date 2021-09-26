from pycat.core import Window, KeyCode
from pycat.sprite import Sprite
from random import randint
from random import random
window=Window(1500,800)
class Owl(Sprite):
    def on_create(self):
        self.scale=0.7+2*random()
        self.opacity=randint(30,70)
        self.image=('owl.gif')
        self.goto_random_position()
    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.D):
            self.x+=5
        if window.is_key_pressed(KeyCode.A):
            self.x-=5
        if window.is_key_pressed(KeyCode.W):
            self.y+=5
        if window.is_key_pressed(KeyCode.S):
            self.y-=5
        if window.is_key_pressed(KeyCode.SPACE):
            ball = window.create_sprite(Ball)
            ball.position = self.position
owl = window.create_sprite(Owl)
class Ball(Sprite):
    def on_create(self):
        self.scale=0.7+2*random()
        self.opacity=randint(50,70)
        self.image=('fireball.gif')
        self.goto_random_position()
    def on_update(self, dt):
        self.x+=5
        if self.x > 1400:
            self.delete()
window.run()