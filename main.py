import cell as c
import cell_pillar as cp
import root as rt
import type

MainRoot = rt.Root(4, list('abcd'))
#print(MainRoot.info())
cells1 = [[0,1],[1,2],[2,2.5]]
cells2 = [[0,0.5],[0.5, 1.5],[1.5,3]]
MainRoot.set_pillar_cells(2, cells1)
MainRoot.set_pillar_cells(1,cells2)
ef = MainRoot.elementary_fragmentation()
#print(ef)
ef_to_c = cp.list_to_cell(ef)
print(ef_to_c)
MainRoot.set_pillar_cells(0,ef_to_c)
print(MainRoot.get_pillar(0).get_cell_wh(3))
