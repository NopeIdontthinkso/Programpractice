from pycat.base.base_sprite import RotationMode
from pycat.core import Window, KeyCode,Scheduler
from pycat.sprite import Sprite
from random import randint, choice
from pyglet.window.key import DELETE, S
window=Window(1500,800,background_image='img/beach_03.png')
class Player(Sprite):
    def on_create(self):
        self.image='img/cat.png'
        self.x=750
        self.y=100
        self.rotation_mode=RotationMode.RIGHT_LEFT
        self.time = 0
    def on_update(self, dt):
#        self.time += dt
#       if self.time > 1:
#           gem = window.create_sprite(Gem)
#            self.time = 0
        if window.is_key_pressed(KeyCode.D):
            self.x+=10
            self.rotation=0
        if window.is_key_pressed(KeyCode.A):
            self.x-=10
            self.rotation=180
class Gem(Sprite):
    def on_create(self):
        self.image=choice(['img/gem_shiny01.png','img/gem_shiny02.png'])
        self.y=800
        self.x=randint(100,1400)
        self.scale=0.2
    def on_update(self, dt):
        self.y -= 3
        if self.y<=50 or self.is_touching_sprite(player):
            self.delete()
def create_gem():
    gem = window.create_sprite(Gem)
Scheduler.update(create_gem,0.5)
player = window.create_sprite(Player)

window.run()