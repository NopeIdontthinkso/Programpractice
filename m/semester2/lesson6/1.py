from pycat.core import Window,Sprite,Color,Label
from typing import List
from random import randint,choice

M,N = 7,7
CELL_SIZE = 75
X0 = CELL_SIZE/2
Y0 = (N-1/2)*CELL_SIZE
A = 0

class End(Label):

    def on_create(self):
        self.color = (0,0,0)
        self.text = 'YOU WIN'

w = Window(height = M*CELL_SIZE, width = N*CELL_SIZE)

class Cell(Sprite):
    def on_create(self):
        self.scale = CELL_SIZE-1
        self.i = 0
        self.j = 0

    def toggle(self):
        global A
        if self.color == (255,0,0):
            self.color = (255,255,255)   
            A -= 1
        else:
            self.color = (255,0,0)
            A += 1  
                        
    def on_left_click(self):
        global A
        if self.j < N-1:
            grid[self.i][self.j+1].toggle()
        if self.j > 0:
            grid[self.i][self.j-1].toggle()
        if self.i > 0:
            grid[self.i-1][self.j].toggle()
        if self.i < M-1:
            grid[self.i+1][self.j].toggle()
        if A == 0:
            w.create_label(End)
        
        
grid:List[List[Cell]]=[]
for i in range(M):
    m = []
    for j in range(N):
        cx = X0 + j*CELL_SIZE
        cy = Y0 - i*CELL_SIZE
        c = w.create_sprite(Cell, x=cx, y=cy)
        c.i = i
        c.j = j
        m.append(c)
    grid.append(m)

for i in range(8):
    choice(choice(grid)).on_left_click()
w.run()

