from pycat.core import Window,Sprite,Color,KeyCode

window = Window()

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
        self.speed = 10
        self.x = window.width/2
        self.y = window.height/2
        self.room = 5
        self.layer = 2

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
        if window.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if window.is_key_pressed(KeyCode.A):
            self.x -= self.speed
        if window.is_key_pressed(KeyCode.D):
            self.x += self.speed

class Map(Sprite):

    def on_create(self):
        self.x = window.width/2
        self.y = window.height/2
    
    def on_update(self, dt):
        self.image = str(player.room) + '.jpg'

player = window.create_sprite(Character)
map = window.create_sprite(Map)

window.run()
        

