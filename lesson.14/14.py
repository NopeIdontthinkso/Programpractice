from pycat.core import Color, KeyCode, Sprite, Window, Scheduler
from random import randint

from pycat.label import Label

window = Window()

class Hp(Label):
    
    def on_update(self, dt: float):
        self.text = 'Hp: '+str(player.hp)

class Score(Label):

    def on_update(self, dt: float):
        self.text = 'Score: '+str(player.score)

class End(Label):

    def on_create(self):
        self.text = 'YOU LOST'

class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 10
        self.x = window.width/2
        self.y = window.height/2
        self.hp = 5
        self.score = 0

    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.W):
            self.y += self.speed
        if window.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if window.is_key_pressed(KeyCode.A):
            self.x -= self.speed
        if window.is_key_pressed(KeyCode.D):
            self.x += self.speed
        if self.hp < 1:
            window.create_label(End, x=300, y=400, font_size=100)
            self.delete()
    
    def on_left_click_anywhere(self):
        b = window.create_sprite(Bullet, position=self.position)
        b.point_toward_mouse_cursor()       

class Bullet(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 10
        self.add_tag('Bullet')
    
    def on_update(self, dt):
        self.move_forward(30)
        if self.is_touching_window_edge():
            self.delete()
        if player.hp <= 1:
            self.delete()

class EnemyBullet(Sprite):

    def on_create(self):
        self.color = Color.RED
        self.scale = 10
    
    def on_update(self, dt):
        self.move_forward(30)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(player):
            player.hp -= 1 
            self.delete()
        if player.hp < 1:
            self.delete()

class Enemy(Sprite):

    def on_create(self):
        self.color = Color.RED
        self.scale = 30
        self.speed = 3
        self.time = 0
        self.position_number = randint(1, 2)
        self.add_tag('Enemy')
        if self.position_number == 1:
            self.x = randint(70, window.width)
            self.y = 70
        else:
            self.x = 70
            self.y = randint(70, window.height)
        self.point_toward_sprite(player)

    def on_update(self, dt):
        self.time += dt
        if self.time >= 1:
            window.create_sprite(EnemyBullet, position=self.position).point_toward_sprite(player)
            self.time = 0
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete() 
        if self.is_touching_any_sprite_with_tag('Bullet'):
            for b in self.get_touching_sprites_with_tag("Bullet"):
                b.delete()
            player.score += 1 
            self.delete()
        if player.hp < 1:
            self.delete()
        
        
def create_enemy(dt):
    if player.hp >= 1:
        window.create_sprite(Enemy)
player = window.create_sprite(Player)
Scheduler.update(create_enemy, 2)
window.create_label(Hp)
window.create_label(Score, y=620)
window.run()