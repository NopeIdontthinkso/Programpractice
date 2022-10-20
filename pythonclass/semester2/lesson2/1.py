from enum import Enum,auto
from pycat.core import Window,Sprite,Color,Scheduler,KeyCode


w=Window(background_image='mountains.png')


GRAVITY = 0.2
SPEED_SCALE = 0.03

class Alienstate(Enum):
    WAIT = auto()
    JUMPING = auto()
    DIE = auto()
    REBORN = auto()

class Bob(Sprite):

    def on_create(self):
        self.image = 'alien.png'
        self.scale = 0.25
        self.state = Alienstate.WAIT
        self.x = f1.x
        self.y = self.y0 = f1.hitbox.y + f1.hitbox.height/2 + self.height/2
        self.y_speed = 0
        self.x_speed = 0
        self.layer = 1

    def on_update(self, dt):
        if self.state is Alienstate.JUMPING:
            self.y_speed -= GRAVITY
            prev_y = self.y
            self.y += self.y_speed
            self.x += self.x_speed
            touch_list = self.get_touching_sprites_with_tag('stop')
            if self.is_touching_window_edge():
                self.state = Alienstate.DIE
            if touch_list:
                p = touch_list[0]
                miny = p.y + p.height/2 + self.height/2
                if prev_y > miny:
                    self.state = Alienstate.WAIT
                    self.y = miny
        if self.state is Alienstate.DIE:
            self.scale -= 0.03
            if self.scale <= 0.01:
                self.state = Alienstate.REBORN
                self.x = f1.x
                self.y = self.y0
        if self.state is Alienstate.REBORN:
            self.scale += 0.03
            if self.scale >= 0.25:
                self.scale = 0.25
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
        self.hitbox = w.create_sprite()
        self.hitbox.add_tag('stop')
        self.hitbox.width = self.width
        self.hitbox.height = 30
        self.hitbox.opacity = 0



f1 = w.create_sprite(Floor, x = 300, y = 100)
f1.hitbox.position = f1.position
f2 = w.create_sprite(Floor, x = 600, y = 400)
f2.hitbox.position = f2.position
f3 = w.create_sprite(Floor, x = 900, y = 100)
f3.hitbox.position = f3.position
w.create_sprite(Bob)

w.run()