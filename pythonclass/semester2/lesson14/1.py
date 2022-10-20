from pycat.core import Window, Sprite
from enum import Enum, auto

class ApeState(Enum):
    WAIT = auto()
    LEFT_UP = auto()
    RIGHT_UP = auto()


w = Window()

class Ape(Sprite):

    def on_create(self):
        self.state = ApeState.WAIT
        self.time = 0
        self.image = 'ape_waiting.png'
        self.throw_time = 0

    def on_update(self, dt):
        self.time += dt
        if self.state == ApeState.WAIT:
            if self.time > 3:
                self.state = ApeState.LEFT_UP
                self.image = 'ape_angry1.png'
                self.time = 0
        if self.state == ApeState.LEFT_UP:
            if self.time > 1:
                self.image = 'ape_angry2.png'
                self.state = ApeState.RIGHT_UP
                self.time = 0
        if self.state == ApeState.RIGHT_UP:
            if self.time > 1:
                if self.throw_time < 4:
                    self.image = 'ape_angry1.png'
                    self.state = ApeState.LEFT_UP
                    w.create_sprite(Barrel, position=self.position)
                    self.throw_time += 1
                    self.time = 0
                else:
                    self.state = ApeState.WAIT
                    self.image = 'ape_waiting.png'
                    self.throw_time = 0
                    self.time = 0


class Barrel(Sprite):

    def on_create(self):
        self.image = 'barrel1.png'
        self.speed = 10
        self.g = 1

    def on_update(self, dt):
        self.speed -= self.g
        self.y += self.speed
        if self.is_touching_window_edge():
            self.delete()
            


a = w.create_sprite(Ape, x=500, y=300)    
        
        
w.run()