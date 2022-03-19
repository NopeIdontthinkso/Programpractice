from pycat.core import Window,Sprite
from random import randint


w = Window(is_sharp_pixel_scaling=True)
ROW = 12
COLS = 24
heatmap = []
CELL_SIZE = 50
X0 = 50
Y0 = 600


for i in range(ROW):
    row = []
    for j in range(COLS):
        row.append(j+COLS*i)
    heatmap.append(row)

class Cell(Sprite):

    def on_left_click(self):
        print(self.image)

for i in range(ROW):
    for j in range(COLS):
        cx = X0 + j*CELL_SIZE
        cy = Y0 - i*CELL_SIZE
        c = w.create_sprite(Cell, x=cx, y=cy)
        numstring = ' '
        if heatmap[i][j] < 10 :
            numstring = '00' + str(heatmap[i][j])
        elif heatmap[i][j] < 100:
            numstring = '0' + str(heatmap[i][j])
        else:
            numstring = str(heatmap[i][j])
        c.image = 'tiles/tile_' + numstring +'.png'
        c.scale_to_width(CELL_SIZE)






print(heatmap)
w.run()