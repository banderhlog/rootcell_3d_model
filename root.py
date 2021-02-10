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
                print(i)
                pillar = cp.CellPillar(self.__pillar_type[i])
                self.__pillars.append(pillar)
        else:
            print('Zero number pillars')

    #возвращает массив клеточных столбов
    def get_pillars(self):
        return self.__pillars

    #устанавливает параметры клеточного столба
    def set_pillar_cells(self, pil_num, cells):
        i = pil_num - 1
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