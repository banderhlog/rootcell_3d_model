# vpython.org
import type
import root as rt
from vpython import *


def draw_root(root: rt.Root):
    scene.background = color.gray(1.9)
    scene.width = 1600
    scene.height = 900
    scene.title = "A display of root cells"
    scene.append_to_caption("""
    To rotate "camera", drag with right button or Ctrl-drag.
    To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
      On a two-button mouse, middle is left + right.
    To pan left/right and up/down, Shift-drag.
    Touch screen: pinch/extend to zoom, swipe or two-finger rotate.""")

    # box(pos = vector(0,0.5,0), length = 0.1, height= 1, width= 0.1, color = color.green, opacity = 0.5)
    # box(pos = vector(0,1.5,0),length = 0.1, height= 1, width= 0.1, color = color.red, opacity = 0.5)
    # box(pos = vector(0,0.5,1), length = 0.1, height= 1, width= 0.1, color = color.green)

    floor = box(pos=vector(0, 0, 0), length=1000, height=0, color=color.white, width=1000)
    pillars = root.get_pillars()

    for i in pillars:

        cells = i.get_cell_pillar()
        print(i.info())
        cells_type = i.get_type()
        center_coordinates = type.center(cells_type)
        tissue = type.type_of_column(cells_type)
        x = center_coordinates[0]
        y = center_coordinates[1]
        current_height = cells[0].get_top() / 2

        if tissue == 'none':
            continue
        elif tissue == 'epidermis':
            length = 13
            width = 13
            cell_color = color.green
        elif tissue == 'cortex':
            length = 5
            width = 5
            cell_color = color.blue
        elif tissue == 'endodermis':
            length = 4
            width = 4
            cell_color = color.purple
        elif tissue == 'red stele':
            length = 2
            width = 2
            cell_color = color.red
        elif tissue == 'blue stele':
            length = 2
            width = 2
            cell_color = color.cyan

        for j in cells:

            cell_bottom = j.get_bottom()
            cell_top = j.get_top()
            cell_height = cell_top - cell_bottom

            if cell_bottom != 0:
                current_height += cell_height / 2

            position = vector(x, current_height, y)
            box(pos=position, length=length, height=cell_height, width=width, color=cell_color, opacity=0.6)
            current_height += cell_height / 2