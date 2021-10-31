from pycat.base.base_sprite import RotationMode
from pycat.core import Window, KeyCode,Scheduler
from pycat.sprite import Sprite
from random import randint, choice


window=Window(background_image='img/sea.png')
label = window.create_label()
label.text = "health"

class Owl(Sprite):
    def on_create(self):
        self.image="img/owl.png"
        self.rotation_mode=RotationMode.RIGHT_LEFT
        self.health=500
    def on_update(self, dt):
        self.move_forward(10)
        if window.is_key_down(KeyCode.LEFT):
            self.rotation=180
        if window.is_key_down(KeyCode.UP):
            self.rotation=90
        if window.is_key_down(KeyCode.RIGHT):
            self.rotation=0
        if window.is_key_down(KeyCode.DOWN):
            self.rotation=270
        if self.is_touching_any_sprite():
            self.health-=1
        if self.health<1:
            print('you die')
            window.close()
        label.text = "health: "+str(self.health)    
class Beach(Sprite):
    def on_create(self):
        self.image=('img/beach.png')
        self.rotation_mode=RotationMode.RIGHT_LEFT
        self.rotation=50
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.rotation-=65


window.create_sprite(Owl)
window.create_sprite(Beach,x=500,y=500)

window.run()