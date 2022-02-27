from enum import Enum,auto
from pycat.core import Window,Sprite,Color,Scheduler,KeyCode


w=Window(background_image='mountains.png')


GRAVITY = 0.2
SPEED_SCALE = 0.03

class Alienstate(Enum):
    WAIT = auto()
    JUMPING = auto()

class Bob(Sprite):

    def on_create(self):
        self.image = 'alien.png'
        self.scale = 0.25
        self.state = Alienstate.WAIT
        self.x = f1.x
        self.y = f1.y + f1.height/2 + self.height/2
        self.y_speed = 0
        self.x_speed = 0

    def on_update(self, dt):
        touch_list = {}
        if self.state is Alienstate.JUMPING:
            self.y_speed -= GRAVITY
            prev_y = self.y
            self.y += self.y_speed
            self.x += self.x_speed
            touch_list = self.get_touching_sprites_with_tag('stop')
            if touch_list:
                p = touch_list[0]
                miny = p.y + p.height/2 + self.height/2
                if self.y_speed < 0:
                    if prev_y > miny:
                        self.state = Alienstate.WAIT
    
    def on_left_click_anywhere(self):
        if self.state is Alienstate.WAIT:
            self.state = Alienstate.JUMPING
            self.x_speed = (w.mouse_position.x - self.x)*SPEED_SCALE
            self.y_speed = (w.mouse_position.y - self.y)*SPEED_SCALE


class Floor(Sprite):

    def on_create(self):
        self.image = 'platform.png'
        self.scale = 0.5
        self.add_tag('stop')



f1 = w.create_sprite(Floor, x = 300, y = 100)
f2 = w.create_sprite(Floor, x = 600, y = 400)
f3 = w.create_sprite(Floor, x = 900, y = 100)
w.create_sprite(Bob)

w.run()