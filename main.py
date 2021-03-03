import cell as c
import cell_pillar as cp
import root as rt
import type
import graphics
types = [1, 2, 3, 4]
MainRoot = rt.Root(4, types)
#print(MainRoot.info())
cells1 = [[0,10]]
cells2 = [[0,5],[5,10],[10,15]]
cells3 = [[0,3],[3,10],[10,15]]
cells4 = [[0,6],[6,10],[10,20]]
MainRoot.set_pillar_cells(0, cells1)
MainRoot.set_pillar_cells(1, cells2)
MainRoot.set_pillar_cells(2, cells3)
MainRoot.set_pillar_cells(3, cells4)
print('-----------------------------')
MainRoot.get_pillars()[2].get_cell(0).info()
ef = MainRoot.elementary_fragmentation()
print(ef)
print(MainRoot.get_types())
MainRoot.metabolism(1)
#print(MainRoot.get_neighbours(1, 0))
print(type.center(0))
graphics.draw_root(MainRoot)