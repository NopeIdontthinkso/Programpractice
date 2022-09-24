from pycat.core import Window,Sprite
from random import randint


w = Window()
ROW = 10
COLS = 10
heatmap = []
CELL_SIZE = 50
X0 = 300
Y0 = 500


for i in range(ROW):
    row = []
    for j in range(COLS):
        row.append(randint(0, 255))
    heatmap.append(row)

class Cell(Sprite):

    def on_create(self):
        self.scale = CELL_SIZE-1
        self.label = w.create_label()

for i in range(ROW):
    for j in range(COLS):
        cx = X0 + j*CELL_SIZE
        cy = Y0 - i*CELL_SIZE
        c = w.create_sprite(Cell, x=cx, y=cy, color=(255,255-heatmap[i][j],255-heatmap[i][j]))
        c.label.text = str(heatmap[i][j])
        c.label.position = c.position
        c.label.x -= c.label.content_width/2
        c.label.y += c.label.content_height/2
        c.label.color = (0,0,0)





print(heatmap)
w.run()