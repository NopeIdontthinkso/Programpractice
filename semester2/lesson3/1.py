from enum import Enum,auto
from pycat.core import Window,Sprite,Color,Scheduler,KeyCode,Color,Label
from random import randint
from pycat.base.event.mouse_event import MouseEvent, MouseButton
from typing import List

w=Window(background_image='mountains.png')


GRAVITY = 0.2
SPEED_SCALE = 0.03

class Hp(Label):
    
    def on_update(self, dt: float):
        self.text = 'Hp: '+str(player.hp)
        self.color = Color.BLACK

class Score(Label):

    def on_update(self, dt: float):
        self.text = 'Score: '+str(player.score)
        self.color = Color.BLACK

class End(Label):

    def on_create(self):
        self.text = 'YOU LOST'
        self.color = Color.BLACK

class Alienstate(Enum):
    WAIT = auto()
    JUMPING = auto()
    DIE = auto()
    REBORN = auto()

class Bob(Sprite):

    def on_create(self):
        self.score = 0
        self.hp = 5
        self.image = 'alien.png'
        self.scale = 0.25
        self.state = Alienstate.WAIT
        self.x = f5.x
        self.y = self.y0 = f5.hitbox.y + f5.hitbox.height/2 + self.height/2
        self.y_speed = 0
        self.x_speed = 0
        self.layer = 1
        w.add_event_subscriber(self)

    def on_update(self, dt):
        if self.state is Alienstate.JUMPING:
            self.y_speed -= GRAVITY
            prev_y = self.y
            self.y += self.y_speed
            self.x += self.x_speed
            touch_list = self.get_touching_sprites_with_tag('stop')
            if self.is_touching_window_edge():
                self.state = Alienstate.DIE
                self.hp -= 1
            if touch_list:
                p = touch_list[0]
                miny = p.y + p.height/2 + self.height/2
                if prev_y > miny:
                    self.state = Alienstate.WAIT
                    self.y = miny
        if self.state is Alienstate.DIE:
            self.scale -= 0.03
            if self.scale <= 0.01: 
                if self.hp < 1:
                    w.create_label(End, x=300, y=400, font_size=100)
                    self.delete()
                self.state = Alienstate.REBORN
                self.x = f5.x
                self.y = self.y0
        if self.state is Alienstate.REBORN:
            self.scale += 0.03
            if self.scale >= 0.25:
                self.scale = 0.25
                self.state = Alienstate.WAIT
        if self.hp < 1:
            self.state = Alienstate.DIE

    def on_mouse_press(self, mouse_event: MouseEvent):
        if mouse_event.button is MouseButton.RIGHT:
            b = w.create_sprite(Bullet, position=self.position)
            b.point_toward_mouse_cursor()
        if mouse_event.button is MouseButton.LEFT:
            if self.state is Alienstate.WAIT:
                self.state = Alienstate.JUMPING
                self.x_speed = (w.mouse_position.x - self.x)*SPEED_SCALE
                self.y_speed = (w.mouse_position.y - self.y)*SPEED_SCALE


class Bullet(Sprite):

    def on_create(self):
        self.color = Color.BLACK
        self.scale = 10
        self.add_tag('Bullet')
    
    def on_update(self, dt):
        self.move_forward(30)
        if self.is_touching_window_edge():
            self.delete()
        if player.hp < 1:
            self.delete()
        

class Monster(Sprite):

    def on_create(self):
        self.position_number = randint(1, 2)
        self.image = 'alien.png'
        self.scale = 0.25
        self.color = Color.RED
        if self.position_number == 1:
            self.x = randint(70, w.width)
            self.y = 70
        else:
            self.x = 70
            self.y = randint(70, w.height)

    def on_update(self, dt):
        self.point_toward_sprite(player)
        self.move_forward(2)
        if self.is_touching_sprite(player):
            player.hp -= 1 
            self.delete()
        if self.is_touching_any_sprite_with_tag('Bullet'):
            for b in self.get_touching_sprites_with_tag("Bullet"):
                b.delete()
            player.score += 1 
            self.delete()
        if player.hp < 1:
            self.delete()


class Floor(Sprite):

    def on_create(self):
        self.image = 'platform.png'
        self.scale = 0.5
        self.add_tag('floor')
        self.hitbox = w.create_sprite()
        self.hitbox.add_tag('stop')
        self.hitbox.width = self.width
        self.hitbox.height = 30
        self.hitbox.opacity = 0

    def on_update(self, dt):
        if player.hp < 1:
            self.delete()


f1 = w.create_sprite(Floor, x = 300, y = 400)
f2 = w.create_sprite(Floor, x = 600, y = 400)
f3 = w.create_sprite(Floor, x = 900, y = 400)
f4 = w.create_sprite(Floor, x = 300, y = 250)
f5 = w.create_sprite(Floor, x = 600, y = 250)
f6 = w.create_sprite(Floor, x = 900, y = 250)
f7 = w.create_sprite(Floor, x = 300, y = 100)
f8 = w.create_sprite(Floor, x = 600, y = 100)
f9 = w.create_sprite(Floor, x = 900, y = 100)
floors: List[Floor] = w.get_sprites_with_tag('floor')
for f in floors:
    f.hitbox.position = f.position
def create_enemy(dt):
    if player.hp > 0:
        w.create_sprite(Monster)
player = w.create_sprite(Bob)
w.create_label(Hp)
w.create_label(Score, y=620)
Scheduler.update(create_enemy, 1)
w.run()