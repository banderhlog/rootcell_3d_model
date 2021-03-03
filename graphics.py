import root as rt
import cell_pillar as cp
import cell as c
import type
from vpython import *

def draw_root(root):
    scene.background = color.gray(1.9)
    scene.width = 1775
    scene.height = 1000
    floor = box(pos=vector(0,0,0), length=1000, height=0, color=color.white, width=1000)
    #box(pos = vector(0,0.5,0), length = 0.1, height= 1, width= 0.1, color = color.green, opacity = 0.5)
    #box(pos = vector(0,1.5,0),length = 0.1, height= 1, width= 0.1, color = color.red, opacity = 0.5)
    #box(pos = vector(0,0.5,1), length = 0.1, height= 1, width= 0.1, color = color.green)
    pillars = root.get_pillars()
    for i in pillars:
        cells = i.get_cell_pillar()
        cells_type = i.get_type()
        center_coordinates = type.center(cells_type)
        x = center_coordinates[0]
        y = center_coordinates[1]
        current_height = cells[0].get_top() / 2
        for j in cells:
            cell_bottom = j.get_bottom()
            cell_top = j.get_top()
            cell_height = cell_top - cell_bottom
            if cell_bottom != 0:
                current_height += cell_height / 2
            position = vector(x, current_height, y)
            box(pos=position, length=15, height=cell_height, width=15, color=color.green, opacity=0.6)
            current_height += cell_height / 2
