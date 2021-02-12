import cell_pillar as cp
import cell as c

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

    #устанавливает параметры клеточного столба
    def set_pillar_cells(self, i, cells):
        self.get_pillars()[i].get_cell_pillar().clear() #удаляем все элементы
        self.get_pillars()[i].set_number_of_cells(len(cells))
        for j in range(len(cells)):
            if j == 0:
                new_cell = c.Cell(0,cells[0][1])
                self.get_pillars()[i].get_cell_pillar().append(new_cell)
            else:
                new_cell = c.Cell(cells[j][0], cells[j][1])
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