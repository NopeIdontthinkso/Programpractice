from pycat.core import Window,AudioLoop,Player
from pycat.sprite import Sprite
from random import shuffle
from typing import List


w=Window(draw_sprite_rects=True,width=1280,height=800,background_image='forest_04.png')
card_list=4*['1.png','2.png','3.png','4.png']
clicked_list: List['Card']=[]
audio_loop=AudioLoop('LoopLivi.wav',volume=0.2)
match_sprite_sound=Player('point.wav')
hit_sprite_sound=Player('hit.wav')
wrong_sprite_sound=Player('laugh.wav')
shuffle(card_list)
audio_loop.play()


class Check(Sprite):
    def on_create(self):
        self.image='button.png'
        self.x=1000
        self.y=400
    def on_left_click(self):
        if len(clicked_list)==2:
            c0=clicked_list[0]
            c1=clicked_list[1]
            if c0.image == c1.image :
                c0.state=1
                c1.state=1
                match_sprite_sound.play()
            else:
                c0.is_visible=False
                c1.is_visible=False
                wrong_sprite_sound.play()
            clicked_list.clear()
    def on_update(self, dt):
        if Card.total==0:
            self.rotation+=2
            self.scale-=0.03
        if self.rotation>=60:
            self.delete()
            w.draw_sprite_rects=False
            w.create_sprite(Win)

        
class Card(Sprite):
    total = 0
    def on_create(self):
        self.image=card_list.pop()
        self.scale=1.5
        self.is_visible=False
        self.state=0
        Card.total+=1
    def on_left_click(self):
        if len(clicked_list)<2:
            if self not in clicked_list:
                self.is_visible=True
                clicked_list.append(self)
                hit_sprite_sound.play()
    def on_update(self, dt):
        if self.state==1:
            self.rotation+=2
            self.scale-=0.05
        if self.rotation>=60:
            self.delete()
            Card.total-=1

class Win(Sprite):
    def on_create(self):
        self.image=('win.png')
        self.x=640
        self.y=400
        self.scale=0
    def on_update(self, dt):
        if self.scale<2:
            self.scale+=0.04
        
        
for a in range(4):
    for i in range(4):
        w.create_sprite(Card,x=100+i*150,y=600-a*150)

w.create_sprite(Check)
w.run()
