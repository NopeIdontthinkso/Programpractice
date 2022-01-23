from random import randint
from pycat.core import Window,Sprite,Color,KeyCode,Label,Scheduler

window = Window(width = 1002 ,height= 1002)

class Hp(Label):

    def on_create(self):
        self.layer = 3
    
    def on_update(self, dt: float):
        self.text = 'Hp: '+str(player.hp)

class Score(Label):

    def on_create(self):
        self.layer = 3

    def on_update(self, dt: float):
        self.text = 'Score: '+str(player.score)

class End(Label):

    def on_create(self):
        self.text = 'YOU LOST'

def nextroom(room , dir):

    if room == 1:
        return {'left': room, 'right': 2, 'up' : room, 'down': 4}[dir]
    elif room == 2:
        return {'left': 1, 'right': 3, 'up' : room, 'down': 5}[dir]
    elif room == 3:
        return {'left': 2, 'right': room, 'up' : room, 'down': 6}[dir]
    elif room == 4:
        return {'left': room, 'right': 5, 'up' : 1, 'down': 7}[dir]
    elif room == 5:
        return {'left': 4, 'right': 6, 'up' : 2, 'down': 8}[dir]
    elif room == 6:
        return {'left': 5, 'right': room, 'up' : 3, 'down': 9}[dir]
    elif room == 7:
        return {'left': room, 'right': 8, 'up' : 4, 'down': room}[dir]
    elif room == 8:
        return {'left': 7, 'right': 9, 'up' : 5, 'down': room}[dir]
    elif room == 9:
        return {'left': 8, 'right': room, 'up' : 6, 'down': room}[dir]

class Character(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 5
        self.x = window.width/2
        self.y = window.height/2
        self.room = 5
        self.layer = 2
        self.hp = 5
        self.score = 0


    def on_update(self, dt):
        if self.y >= window.height:
            r = nextroom(self.room, 'up')
            if r == self.room:
                self.y = window.height-1
            else:
                self.y = 1
                self.room = r
        if self.y <= 0:
            r = nextroom(self.room, 'down')
            if r == self.room:
                self.y = 1
            else:
                self.room = r
                self.y = window.height - 1
        if self.x >= window.width:
            r = nextroom(self.room, 'right')
            if r == self.room:
                self.x = window.width-1
            else:
                self.x = 1
                self.room = r
        if self.x <= 0:
            r = nextroom(self.room, 'left')
            if r == self.room:
                self.x = 1
            else:
                self.room = r
                self.x = window.width - 1
        if window.is_key_pressed(KeyCode.W):
            self.y += self.speed
            if self.is_touching_any_sprite_with_tag('wall'):
                self.y -= self.speed
        if window.is_key_pressed(KeyCode.S):
            self.y -= self.speed
            if self.is_touching_any_sprite_with_tag('wall'):
                self.y += self.speed
        if window.is_key_pressed(KeyCode.A):
            self.x -= self.speed
            if self.is_touching_any_sprite_with_tag('wall'):
                self.x += self.speed
        if window.is_key_pressed(KeyCode.D):
            self.x += self.speed
            if self.is_touching_any_sprite_with_tag('wall'):
                self.x -= self.speed

        if self.room == 1:
            visibility = [True, True, True, True, False, False, True, False, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]
        if self.room == 2:
            visibility = [True, True, True, False, False, False, True, False, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]
        if self.room == 3:
            visibility = [True, True, True, False, False, True, True, False, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]
        if self.room == 4:
            visibility = [True, False, True, True, False, False, True, False, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]        
        if self.room == 5:
            visibility = [True, False, True, False, False, False, True, False, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]
        if self.room == 6:
            visibility = [True, False, True, False, False, True, True, False, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]
        if self.room == 7:
            visibility = [True, False, True, True, False, False, True, True, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]
        if self.room == 8:
            visibility = [True, False, True, False, False, False, True, True, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]
        if self.room == 9:
            visibility = [True, False, True, False, False, True, True, True, True]
            for i in range(9):
                walls[i].is_visible = visibility[i]

        if self.hp < 1:
            window.create_label(End, x=150, y=600, font_size=100)
            self.delete()

    def on_left_click_anywhere(self):
        b = window.create_sprite(Bullet, position=self.position)
        b.point_toward_mouse_cursor()

class Wall(Sprite):

    def on_create(self):
        self.color = Color.AZURE
        self.scale = window.width/3
        self.layer = 2
        self.add_tag('wall')

    def on_update(self, dt):
        if player.hp < 1:
            self.delete()

class Bullet(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 10
        self.add_tag('Bullet')
        self.room = player.room
    
    def on_update(self, dt):
        if player.room == self.room:
            self.is_visible = True
        else:
            self.is_visible = False
        self.move_forward(30)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag('wall'):
            self.delete()
        if player.hp < 1:
            self.delete()

class Enemy(Sprite):

    def on_create(self):
        self.color = Color.RED
        self.scale = 30
        self.speed = 3
        self.time = 0
        self.add_tag('Enemy')
        self.room = randint(1,9)
        if player.room == self.room:
            self.is_visible = True
        else:
            self.is_visible = False
            self.y = randint(window.height/3+30,(window.height*2)/3-30)
            self.x = randint(window.width/3+30,(window.width*2/3)-30)
        if self.is_touching_any_sprite_with_tag('wall'):
            window.create_sprite(Enemy)
            self.delete()
        self.point_toward_sprite(player)

    def on_update(self, dt):
        if player.room == self.room:
            self.is_visible = True
        else:
            self.is_visible = False
        if self.is_visible == True:
            self.time += dt
            if self.time >= 1:
                window.create_sprite(EnemyBullet, position=self.position).point_toward_sprite(player)
                self.time = 0
            self.move_forward(self.speed)
            if self.is_touching_window_edge() or self.is_touching_any_sprite_with_tag('wall'):
                self.rotation -= 90
                
            if self.is_touching_any_sprite_with_tag('Bullet'):
                for b in self.get_touching_sprites_with_tag("Bullet"):
                    b.delete()
                player.score += 1 
                self.delete()
        if player.hp < 1:
            self.delete()

class EnemyBullet(Sprite):

    def on_create(self):
        self.color = Color.RED
        self.scale = 10
        self.room = player.room
    
    def on_update(self, dt):
        if player.room == self.room:
            self.is_visible = True
        else:
            self.is_visible = False
        self.move_forward(30)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag("wall"):
            self.delete()
        if self.is_touching_sprite(player):
            player.hp -= 1 
            self.delete()
        if player.hp < 1:
            self.delete()

player = window.create_sprite(Character)

w1 = window.create_sprite(Wall, x=window.width/6, y=(window.height*5)/6)
w2 = window.create_sprite(Wall, x=(window.width*3)/6, y=(window.height*5)/6)
w3 = window.create_sprite(Wall, x=(window.width*5)/6, y=(window.height*5)/6)
w4 = window.create_sprite(Wall, x=window.width/6, y=(window.height*3)/6)
w5 = window.create_sprite(Wall, x=(window.width*3)/6, y=(window.height*3)/6)
w6 = window.create_sprite(Wall, x=(window.width*5)/6, y=(window.height*3)/6)
w7 = window.create_sprite(Wall, x=window.width/6, y=window.height/6)
w8 = window.create_sprite(Wall, x=(window.width*3)/6, y=window.height/6)
w9 = window.create_sprite(Wall, x=(window.width*5)/6, y=window.height/6)

walls = [w1, w2, w3, w4, w5, w6, w7, w8, w9]

window.create_label(Hp)
window.create_label(Score, y=980)
def create_enemy(dt):
    if player.hp >= 1:
        window.create_sprite(Enemy)
Scheduler.update(create_enemy, 4)

window.run()
        

