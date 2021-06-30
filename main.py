import root as rt
import graphics
'''
types = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MainRoot = rt.Root(9, types)
cells1 = [[0, 5], [5, 10], [10, 15]]
cells2 = [[0, 5], [5, 10], [10, 15]]
cells3 = [[0, 5], [5, 10], [10, 15]]
cells4 = [[0, 5], [5, 10], [10, 15]]
cells5 = [[0, 5], [5, 10], [10, 15]]
cells6 = [[0, 5], [5, 10], [10, 15]]
cells7 = [[0, 5], [5, 10], [10, 15]]
cells8 = [[0, 5], [5, 10], [10, 15]]
cells9 = [[0, 5], [5, 10], [10, 15]]

#cells3 = [[0, 6], [6, 10]]
# cells6 = [[0, 4], [4, 10]]
MainRoot.set_pillar_cells(0, cells1)
#MainRoot.info()
MainRoot.set_pillar_cells(1, cells2)
MainRoot.set_pillar_cells(2, cells3)
MainRoot.set_pillar_cells(3, cells4)
MainRoot.set_pillar_cells(4, cells5)
MainRoot.set_pillar_cells(5, cells6)
MainRoot.set_pillar_cells(6, cells7)
MainRoot.set_pillar_cells(7, cells8)
MainRoot.set_pillar_cells(8, cells9)
#MainRoot.set_pillar_cells(2, cells3)
# MainRoot.set_pillar_cells(3, cells6)
#new_subst = [[[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]]]
#new_subst = [[[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]]]
#new_subst = [[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [1, 1, 1]], [[0, 0, 0], [0, 0, 0]]]
new_subst = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    , [[0, 0, 0], [0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
             [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
MainRoot.set_substance(new_subst)
for i in range(75):
    MainRoot.new_metabolism(1)
print('------------------')
print('result', MainRoot.get_substance())
#print('info', MainRoot.info())
graphics.draw_root(MainRoot)

'''
types = list(range(1, 80))
MainRoot = rt.Root(79, types)

MainRoot.set_root(100, 20)
MainRoot.new_metabolism(1)
print(MainRoot.get_substance())
graphics.draw_root(MainRoot)

