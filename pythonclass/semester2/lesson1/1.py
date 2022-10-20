from pycat.core import Window,Sprite,Scheduler,KeyCode
from random import randint


w=Window(enforce_window_limits=False, width=1800, height=808, background_image='background.png')
w.background_sprite.scale*=2
pipe_gap = 400
min_pipe_y = -200
b = 1.75

class Pipe(Sprite):

    def on_create(self):
        self.image = "pipe.png"
        self.x = w.width + self.width/2
        self.add_tag('pipe')

    def on_update(self, dt):
        pipe_speed = 525/(b*60)
        self.x -= pipe_speed
        if self.x <= -self.width/2:
            self.delete()

class Bird(Sprite):

    def on_create(self):
        self.image = 'bird.gif'
        self.x = w.width/2
        self.y = w.height/2
        self.scale = 0.4
        self.fall = 0

    def on_update(self, dt):
        if w.is_key_down(KeyCode._1):
            w.save_screen_shot("img.png")
        self.y -= self.fall
        if self.fall <= 3.5/b:
            self.fall +=0.525/b
        if w.is_key_down(KeyCode.SPACE):
            self.fall = -10.5/b
        if self.is_touching_any_sprite_with_tag('pipe'):
            w.close()
            

db = 0.05
def pipecreate(dt):
    global b
    a = randint(0, w.height/2)
    pipe_down = w.create_sprite(Pipe, y=min_pipe_y + a)
    pipe_up = w.create_sprite(Pipe, y = min_pipe_y+ pipe_gap + pipe_down.height + a, rotation = 180)
    b -= db
    Scheduler.update(pipecreate2, b)
    Scheduler.cancel_update(pipecreate)

def pipecreate2(dt):
    global b
    a = randint(0, w.height/2)
    pipe_down = w.create_sprite(Pipe, y=min_pipe_y + a)
    pipe_up = w.create_sprite(Pipe, y = min_pipe_y+ pipe_gap + pipe_down.height + a, rotation = 180)
    b -= db
    Scheduler.update(pipecreate, b)
    Scheduler.cancel_update(pipecreate2)

w.create_sprite(Bird)
Scheduler.update(pipecreate, b)


w.run()

