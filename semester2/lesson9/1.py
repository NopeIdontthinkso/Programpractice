from pycat.core import Window, Sprite, Color, KeyCode
from random import choice


w = Window(draw_sprite_rects= True)
COLORS = [Color.RED, Color.AMBER, Color.BLUE, Color.GREEN, Color.AZURE, Color.CYAN, Color.BLACK, Color.PURPLE]
PEG = 4
GUESS = 5
chosen_color = Color.BLACK
SCALE = 75
TIME = 0


class ColorSprite(Sprite):
    def on_create(self):
        self.scale = SCALE


class ChoiceSprite(Sprite):
    def on_create(self):
        self.scale = SCALE/2
        self.x = self.width/2
    def on_left_click(self):
        global chosen_color
        chosen_color = self.color


class SecretCode:
    def __init__(self):
        self.colors = [choice(COLORS) for _ in range(PEG)]
        self.sprite = [w.create_sprite(ColorSprite, color=c, x=SCALE/2, y=600) for c in self.colors]
        for i in range(PEG):
            self.sprite[i].x += self.sprite[i].scale*i


class ColorChooser:
    def __init__(self):
        self.sprite = [w.create_sprite(ChoiceSprite, color=c, y=100) for c in COLORS]
        for i in range(len(COLORS)):
            self.sprite[i].x += self.sprite[i].scale*i


class GuessSprite(ColorSprite):
    def on_left_click(self):
        self.color = chosen_color
    def on_update(self, dt):
        global GUESS
        global TIME
        if TIME < GUESS:
            if w.is_key_down(KeyCode.ENTER):
                w.create_sprite(ColorSprite, position = self.position, color = self.color)
                self.y += self.scale
                


class Guess:
    def __init__(self):
        self.sprite = [w.create_sprite(GuessSprite, x=SCALE/2, y=200, color=Color.BLACK) for _ in range(PEG)]
        for i in range(PEG):
            self.sprite[i].x += self.sprite[i].scale*i


def key(key: KeyCode):
    global GUESS
    global TIME
    if TIME < GUESS:
        if key==KeyCode.ENTER:
            red = 0
            white = 0
            for i in range(PEG):
                for j in range(PEG):
                    if g.sprite[i].color == s.sprite[j].color:
                        if i == j:
                            red += 1
                        else:
                            white += 1 
            print('red='+str(red), 'white='+str(white))
            TIME += 1


s = SecretCode()
ColorChooser()
g = Guess()
w.run(on_key_press=key)