from pycat.base.base_sprite import RotationMode
from pycat.core import Window, KeyCode,Scheduler
from pycat.sprite import Sprite
from random import randint, choice,shuffle
from typing import List

from pyglet.clock import schedule


w=Window(draw_sprite_rects=True,width=1280,height=800)
card_list=4*['1.png','2.png','3.png','4.png']
clicked_list: List['Card']=[]
shuffle(card_list)


#class Check(Sprite):
    #def on_create(self):
        #self.image='button.png'
        #self.x=1000
        #self.y=400
    #def on_update(self):
        #if len(clicked_list)==2:
            #c0=clicked_list[0]
           # c1=clicked_list[1]
            #if c0.image == c1.image :
                #c0.delete()
                #c1.delete()
            #else:
                #c0.is_visible=False
                #c1.is_visible=False
            #clicked_list.clear()

        
class Card(Sprite):
    def on_create(self):
        self.image=card_list.pop()
        self.scale=1.5
        self.is_visible=False
    def on_left_click(self):
        if len(clicked_list)<2:
            self.is_visible=True
            clicked_list.append(self)


#w.create_sprite(Check)        
for a in range(4):
    for i in range(4):
        w.create_sprite(Card,x=100+i*150,y=600-a*150)


def check_match(dt):
    if len(clicked_list)==2:
        a0=dt+2
        if dt==a0:
            c0=clicked_list[0]
            c1=clicked_list[1]
            if c0.image == c1.image :
                c0.delete()
                c1.delete()
            else:
                c0.is_visible=False
                c1.is_visible=False
            clicked_list.clear()
Scheduler.update(check_match)

w.run()