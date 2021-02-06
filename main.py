import cell as c
import cell_pillar as cp

new_cell = c.Cell(0, 1)
n = cp.CellPillar('main',2)
print(n.info())
n.insert_cell(0.5, 4)
print(n.info())