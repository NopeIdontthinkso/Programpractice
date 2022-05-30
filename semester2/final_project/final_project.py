from pycat.core import Window, Sprite, Color, Scheduler, Label, KeyCode
from enum import Enum, auto
from random import choice, randint
from os.path import dirname


w = Window(enforce_window_limits=False)


class PlayerState(Enum):
    WAIT = auto()
    JUMP = auto()


class HollowKnight(Sprite):


    def on_create(self):
        self.scale = 50
        self.color = Color.RED
        self.state = PlayerState.WAIT
        self.g = 0.2
        self.fall = 0
        self.jump_time = 0
    
    def on_update(self, dt):
        if self.state == PlayerState.JUMP:
            self.y -= self.fall
            if w.is_key_down(KeyCode.SPACE) and self.jump_time < 2:
                self.fall = -8
                self.jump_time += 1
            if self.fall < 10:
                self.fall += self.g
            if self.is_touching_any_sprite_with_tag('floor') and self.fall>0:
                self.state = PlayerState.WAIT
                self.fall = 0
                self.jump_time = 0
        if self.state == PlayerState.WAIT:
            if w.is_key_down(KeyCode.SPACE):
                self.state = PlayerState.JUMP
                self.fall = -8
                self.jump_time += 1
        if w.is_key_pressed(KeyCode.LEFT):
            pass


class Backgound_floor(Sprite):


    def on_create(self):
        self.height = 300
        self.width = 2000
        self.color = Color.WHITE
        self.add_tag('floor')

    def on_update(self, dt):
        pass
            


player = w.create_sprite(HollowKnight, x=500, y=300)
backgound_floor = w.create_sprite(Backgound_floor, x=500, y=-100)


w.run()