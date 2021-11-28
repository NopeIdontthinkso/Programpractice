from pycat.base.color import Color
from pycat.core import Window, Label, Sprite

map_list=[
    'L11_media/1.jpg',
    'L11_media/2.jpg',
    'L11_media/3.jpg',
    'L11_media/4.jpg',
    'L11_media/5.jpg',
    'L11_media/6.jpg',
    'L11_media/7.jpg',
    'L11_media/8.jpg',
    'L11_media/9.jpg',
    'L11_media/10.jpg'
]
title_list=[
    'bus',
    'bus2',
    'bus3',
    'stone(?',
    'leaves',
    'bus4',
    'strawberry',
    'shark',
    'whateveritis',
    'whateveritis2'
]

w=Window(width=1280,height=800)

class Next(Sprite):
    def on_create(self):
        self.image = 'L11_media/button_next.png'
        self.map_now = 0
        w.background_image=map_list[0]
        title.text=title_list[0]

    def on_left_click(self):
        if self.map_now<(len(map_list)-1):
            self.map_now+=1
        else:
            self.map_now=0
        w.background_image=map_list[self.map_now]
        title.text=title_list[self.map_now]
        title.font_size=0


class Title(Label):
    def on_create(self):
        self.x=w.width/2
        self.font_size=0
    def on_update(self, dt: float):
        if self.font_size<50:
            self.font_size+=1
        r,g,b = self.color
        r-=1
        g-=1
        b-=1
        self.color = Color(r,g,b) 
        
    
title=w.create_label(Title)

w.create_sprite(Next,x=640,y=200)
w.run()