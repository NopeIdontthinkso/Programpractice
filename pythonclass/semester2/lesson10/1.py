from pycat.core import Window, Sprite, Color, KeyCode
from random import choice


w = Window(draw_sprite_rects= True)
COLORS = [Color.RED, Color.AMBER, Color.BLUE, Color.GREEN, Color.AZURE, Color.CYAN, Color.BLACK, Color.PURPLE]
PEG = 4
GUESS = 10
chosen_color = Color.BLACK
SCALE = 35
time = 0


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
        self.sprite = [w.create_sprite(ColorSprite, color=c, x=SCALE/2, y=600, is_visible = False) for c in self.colors]      
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
        global time
        if time < GUESS:
            if w.is_key_down(KeyCode.ENTER):
                w.create_sprite(ColorSprite, position = self.position, color = self.color)
                self.y += self.scale
                

class Guess:
    def __init__(self):
        self.sprite = [w.create_sprite(GuessSprite, x=SCALE/2, y=200, color=Color.BLACK) for _ in range(PEG)]
        for i in range(PEG):
            self.sprite[i].x += self.sprite[i].scale*i
    
    @property
    def y(self):
        return self.sprite[0].y


def key(key: KeyCode):
    global GUESS
    global time
    if time < GUESS:
        if key == KeyCode.ENTER:
            red = 0
            white = 0
            white_guess = []
            white_code = [] 
            for i in range(PEG):
                if code.sprite[i].color == guess.sprite[i].color:
                        red += 1
                else:
                    white_code.append(code.sprite[i].color)
                    white_guess.append(guess.sprite[i].color)
            for color in  white_guess:
                if color in white_code:
                    white += 1
                    white_code.remove(color)
            a = (PEG+1)*SCALE
            for i in range(red):
                b = w.create_sprite(ColorSprite, color=Color.RED, x=a, y=guess.y, scale = SCALE/2)
                a += b.scale
            for i in range(white):
                b = w.create_sprite(ColorSprite, color=Color.WHITE, x=a, y=guess.y, scale = SCALE/2)
                a += b.scale
            time += 1
            if red == 4:
                for i in code.sprite:
                    i.is_visible = True
                print('you win')
            elif time == GUESS:
                for i in code.sprite:
                    i.is_visible = True
                if red != 4:
                    print('you lose')


code = SecretCode()
ColorChooser()
guess = Guess()
w.run(on_key_press=key)