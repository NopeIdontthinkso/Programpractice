from pycat.core import Window
from random import randint

ROW = 3
COLS = 3
heatmap = []


for i in range(ROW):
    row = []
    for j in range(COLS):
        row.append(randint(0, 255))
    heatmap.append(row)

print(heatmap)
