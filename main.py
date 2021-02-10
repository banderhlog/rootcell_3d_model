import cell as c
import cell_pillar as cp
import root as rt

MainRoot = rt.Root(4, list('abcd'))
#print(MainRoot.info())
cells = [[0,1],[1,2],[2,2.5]]
MainRoot.set_pillar_cells(2, cells)
print(MainRoot.info())