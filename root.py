import cell_pillar as cp
import cell
import type
import numpy as np
from scipy.integrate import odeint

#класс корня
class Root:

    #конструктор – представляет из себя массив клеточных столбов
    def __init__(self, num_of_pillars, pillar_type):
        if num_of_pillars > 0:
            self.__num_of_pillars = num_of_pillars
            self.__pillar_type = pillar_type
            self.__pillars = []
            for i in range(num_of_pillars):
                pillar = cp.CellPillar(self.__pillar_type[i])
                self.__pillars.append(pillar)
        else:
            print('Zero number pillars')

    #возвращает массив клеточных столбов
    def get_pillars(self):
        return self.__pillars

    #возвращает i-тый клеточный столб
    def get_pillar(self,i):
        return self.__pillars[i]

    #возвращает j-тую клетку i-того столба
    def get_cell(self, i, j):
        return self.__pillars[i].get_cell(j)

    #возвращает массив типов клеточных столбов
    def get_types(self):
        return self.__pillar_type

    #устанавливает параметры клеточного столба
    def set_pillar_cells(self, i, cells):
        self.get_pillars()[i].get_cell_pillar().clear() #удаляем все элементы
        self.get_pillars()[i].set_number_of_cells(len(cells))
        for j in range(len(cells)):
            if j == 0:
                new_cell = cell.Cell(0,cells[0][1])
                self.get_pillars()[i].get_cell_pillar().append(new_cell)
            else:
                new_cell = cell.Cell(cells[j][0], cells[j][1])
                self.get_pillars()[i].get_cell_pillar().append(new_cell)

    #информация о корне
    def info(self):
        for i in self.get_pillars():
            i.info()

    #возвращает массив значений, разбивающий корень
    #на элементарный разрезы
    def elementary_fragmentation(self):
        res = []
        for i in self.get_pillars():
            if i.get_number_of_cells() != 0:
                res.append(i.cell_to_list())
        b = []
        for i in range(len(res)):
            b += list(res[i])
        b = sorted(list(set(b)))
        return b

    #поиск соседей j-той клетки i-того клеточного столба
    def get_neighbours(self, i, j):
        res = {}
        c = self.get_cell(i,j)
        type_of_pillar = self.get_pillar(i).get_type()
        neighbour_pillars_all = type.neighbours(type_of_pillar)
        neighbour_pillars = []
        cell_fragmentation = [c.get_bottom(), c.get_top()]

        for n in neighbour_pillars_all:
            if n[0] in self.get_types():
                neighbour_pillars.append(n)

        fragmentation = self.elementary_fragmentation()

        for fragment in fragmentation:
            if cell_fragmentation[0] < fragment < cell_fragmentation[1]:
                cell_fragmentation.append(fragment)

        cell_fragmentation = sorted(cell_fragmentation)
        cell_fragmentation = cp.list_to_cell(cell_fragmentation)

        for neighbour in neighbour_pillars:
            #print(neighbour)
            cell_index = []
            for cell_fragment in cell_fragmentation:
                local_pillar = self.get_pillar(neighbour[0] - 1)
                local_cell = local_pillar.get_cell_wh(cell_fragment[0])
                if local_cell not in cell_index and local_cell != -1:
                    cell_index.append(local_cell)
            #print('соседи для',neighbour,'это',cell_index)
            res.update({neighbour[0]:cell_index})

        #print(fragmentation)
        #print(neighbour_pillars)
        #print(cell_fragmentation)
        return res



    #обмен веществ между клеточыми столбами
    def metabolism(self, t):
        i = 0
        for p in self.get_pillars():
            j = 0
            for c in p.get_cell_pillar():
                print(i,j)
                print(self.get_neighbours(i, j))
                j += 1
            i +=1
