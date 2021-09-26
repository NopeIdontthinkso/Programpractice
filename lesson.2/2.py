from pycat.core import Window
from pycat.sprite import Sprite
from random import randint
from random import random
class Owl(Sprite):
    def on_create(self):
        self.scale=0.7+2*random()
        self.opacity=randint(30,70)
        self.image=('owl.gif')
        self.goto_random_position()
class Ball(Sprite):
    def on_create(self):
        self.scale=0.7+2*random()
        self.opacity=randint(50,70)
        self.image=('fireball.gif')
        self.goto_random_position()
window=Window(1500,800)
for _ in range(100):
    window.create_sprite(Owl)
    window.create_sprite(Ball)
window.run()