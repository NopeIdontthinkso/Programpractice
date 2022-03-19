from pycat.core import Window,Sprite
from typing import List, Dict

def levelbuild(level:List[str], level_d:Dict[str,str], cell_size:int, x0:int, y0:int, tag:str, window: Window):
    class Cell(Sprite):

        def on_create(self):
            self.add_tag(tag)

        def on_left_click(self):
            print(self.image)

    for i in range(len(level)):
        for j in range(len(level[i])):
            cx = x0 + j*cell_size
            cy = y0 - i*cell_size
            c = window.create_sprite(Cell, x=cx, y=cy, image = level_d[level[i][j]][0])
            c.add_tag(level_d[level[i][j]][1])
            c.scale_to_width(cell_size)
