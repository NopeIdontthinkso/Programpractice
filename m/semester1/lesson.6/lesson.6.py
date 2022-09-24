from pycat.base.base_sprite import RotationMode
from pycat.core import Window, KeyCode,Scheduler
from pycat.sprite import Sprite
from random import randint, choice

w=Window(width=1280,height=800,background_image='underwater_04.png')
scorelabel = w.create_label()

class Spaceship(Sprite):
    score = 0
    def on_create(self):
        self.image = 'saucer.png'
        self.scale = 0.3
        self.y = 700
        self.x = 60
        self.rotation = 0 
        self.rotation_mode = RotationMode.RIGHT_LEFT

    def on_update(self, dt):
        self.move_forward(5)
        scorelabel.text = 'score:' + str(self.score)
        if (self.x>1200) or (self.x<50):
            self.rotation += 180

class Monster(Sprite):
    a = 30
    def on_create(self):
        self.image = choice(['1.png','2.png','3.png','4.png','5.png'])
        self.state = 0
        self.scale = 0.5

    def on_left_click(self):
        self.state = 1
    
    def on_update(self, dt):
        if self.is_touching_sprite(ss):
            self.delete()
            Spaceship.score += 1        
        if self.state == 0:
            if self.x > 1200:
                self.delete()
            else:
                self.x += 5
                self.y += self.a
                self.a -= 1.5
                if self.y < 100:
                    self.a = 30
        else:
            if self.y > 750:
                self.delete()
            else:
                self.y += 10

def create_monster():
    w.create_sprite(Monster,y = 100)

Scheduler.update(create_monster,1)
ss = w.create_sprite(Spaceship)

w.run()