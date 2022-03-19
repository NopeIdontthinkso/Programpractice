from pycat.core import Window,Sprite,KeyCode,Color
from levelbuild import levelbuild


w = Window(is_sharp_pixel_scaling=True)


CELL_SIZE = 50
X0 = 100
Y0 = 500
LEVEL = [
            'gggggggggg',
            'ggwwwwwwgg',
            'ggwggggwgg',
            'ggwggggwgg',
            'ggwggggwgg',
            'ggwggggggg',
            'ggwggggggg',
            'ggwggggggg',
            'ggwggggggg',
            'gggggggggg'
        ]


LEVEL_D = { 'g': ('tiles/tile_053.png', 'g'),
            'w': ('tiles/tile_012.png', 'w')
          }


class Player(Sprite):

    def on_create(self):
        self.scale = 30
        self.speed = 5
        self.x = w.width/2
        self.y = w.height/2
        self.room = 5
        self.layer = 2
        self.hp = 5
        self.score = 0
        self.image = 'tiles/tile_190.png'
        self.scale_to_width(CELL_SIZE)


    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.W):
            self.y += self.speed
            if self.is_touching_any_sprite_with_tag('w'):
                self.y -= self.speed
        if w.is_key_pressed(KeyCode.S):
            self.y -= self.speed
            if self.is_touching_any_sprite_with_tag('w'):
                self.y += self.speed
        if w.is_key_pressed(KeyCode.A):
            self.x -= self.speed
            if self.is_touching_any_sprite_with_tag('w'):
                self.x += self.speed
        if w.is_key_pressed(KeyCode.D):
            self.x += self.speed
            if self.is_touching_any_sprite_with_tag('w'):
                self.x -= self.speed

player = w.create_sprite(Player)
levelbuild(level=LEVEL, level_d=LEVEL_D, cell_size=CELL_SIZE, x0=X0, y0=Y0, window=w, tag= 'level1')

w.run()