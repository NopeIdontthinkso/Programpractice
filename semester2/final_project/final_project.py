from pycat.core import Window, Sprite, Color, Scheduler, Label, KeyCode
from enum import Enum, auto
from random import choice, randint
from os.path import dirname


w = Window(enforce_window_limits=False)


class PlayerState(Enum):
    WAIT = auto()
    JUMP = auto()
    WALK = auto()
    FLY = auto()
    


class HollowKnight(Sprite):


    def on_create(self):
        self.scale = 50
        self.color = Color.RED
        self.state = PlayerState.JUMP
        self.g = 0.2
        self.y_speed = 0
        self.jump_time = 0
        self.speed = 10
    
    def on_update(self, dt):
        print(self.state)
        if self.state is PlayerState.JUMP:
            self.y -= self.y_speed
            if w.is_key_pressed(KeyCode.RIGHT) or w.is_key_pressed(KeyCode.LEFT):
                self.state = PlayerState.FLY
            if w.is_key_down(KeyCode.UP) and self.jump_time < 2:
                self.y_speed = -8
                self.jump_time += 1
            if self.y_speed < 10:
                self.y_speed += self.g
            if self.is_touching_any_sprite_with_tag('floor') and self.y_speed>0:
                self.state = PlayerState.WAIT
                self.y_speed = 0
                self.jump_time = 0

        #jump state
        if self.state is PlayerState.WAIT:
            if w.is_key_down(KeyCode.UP):
                self.state = PlayerState.JUMP
                self.y_speed = -8
                self.jump_time += 1
            if self.move_left_right_if_press_keys():
                self.state = PlayerState.WALK
        
        # waiting state
        if self.state is PlayerState.WALK:
            if w.is_key_pressed(KeyCode.UP):
                self.state = PlayerState.FLY
            if not self.move_left_right_if_press_keys():
                self.state = PlayerState.WAIT

        #walk 
        if self.state is PlayerState.FLY:
            self.y -= self.y_speed
            if w.is_key_down(KeyCode.UP) and self.jump_time < 2:
                self.y_speed = -8
                self.jump_time += 1
            if self.y_speed < 10:
                self.y_speed += self.g
            if self.is_touching_any_sprite_with_tag('floor') and self.y_speed>0:
                self.state = PlayerState.WAIT
                self.y_speed = 0
                self.jump_time = 0
            if not self.move_left_right_if_press_keys():
                self.state = PlayerState.JUMP

        #fly


    def move_left_right_if_press_keys(self):
        if w.is_key_pressed(KeyCode.LEFT):
            self.x -= self.speed
            return True
        if w.is_key_pressed(KeyCode.RIGHT):
            self.x += self.speed
            return True
        return False

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