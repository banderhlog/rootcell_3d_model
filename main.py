import root as rt
import graphics

types = [1, 2]
MainRoot = rt.Root(2, types)
cells1 = [[0, 3], [3, 10]]
cells2 = [[0, 5], [5, 10]]
cells3 = [[0, 5], [5, 10]]
#cells3 = [[0, 6], [6, 10]]
# cells6 = [[0, 4], [4, 10]]
MainRoot.set_pillar_cells(0, cells1)
#MainRoot.info()
MainRoot.set_pillar_cells(1, cells2)
#MainRoot.set_pillar_cells(2, cells3)
# MainRoot.set_pillar_cells(3, cells6)
#new_subst = [[[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]]]
#new_subst = [[[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]]]
#new_subst = [[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [1, 1, 1]], [[0, 0, 0], [0, 0, 0]]]
new_subst = [[[0, 0, 0], [1, 1, 1]], [[0, 0, 0], [0, 0, 0]]]
MainRoot.set_substance(new_subst)
for i in range(1):
    MainRoot.metabolism(1)
print('------------------')
print('result', MainRoot.get_substance())
#print('info', MainRoot.info())
graphics.draw_root(MainRoot)

'''
types = list(range(1, 80))
MainRoot = rt.Root(79, types)

MainRoot.set_root(10, 2)
MainRoot.metabolism(1)
print(MainRoot.get_substance())
graphics.draw_root(MainRoot)
'''