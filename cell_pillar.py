#класс столб клеток
import cell as c

class CellPillar:

    #конструктор - представляет из себя массив клеток
    def __init__(self, type, number_of_cells):
        if number_of_cells > 0:
            self.__type = type
            self.__number_of_cells = number_of_cells
            self.__cell_pillar = []
            for i in range(number_of_cells):
                local_cell = c.Cell(i, i + 1)
                self.__cell_pillar.append(local_cell)
        else:
            print('Zero number of cells\n')

    #возвращает тип клеточного столба
    def get_type(self):
        return self.__type

    #возвращет количество клеток в клеточном столбе
    def get_number_of_cells(self):
        return self.__number_of_cells

    #возвращает массив клеток
    def get_cell_pillar(self):
        return self.__cell_pillar

    #возвращает i-тую клетку из столба, считая снизу
    def get_cell(self, i):
        return self.__cell_pillar[i]

    #устанавливает высоту i-той клетки и обновляет высоту клеток выше
    def set_new_top(self, i, new_height):
        if i >= 0 and i < self.__number_of_cells:
            old_bottom = self.__cell_pillar[i].get_bottom()
            old_top = self.__cell_pillar[i].get_top()
            old_height = old_top - old_bottom
            if old_height < 0:
                print('Impossible height, pillar ',self.__type,'i=', i)
            difference = new_height - old_height
            self.__cell_pillar[i].set_top(old_top + difference)
            for j in range(i + 1, self.__number_of_cells):
                self.__cell_pillar[j].set_top(self.__cell_pillar[j].get_top() + difference)
                self.__cell_pillar[j].set_bottom(self.__cell_pillar[j].get_bottom() + difference)

    #вставка клетки в столб
    def insert_cell(self, size, position):
        if position >= 0 and position <= self.__number_of_cells:
            z0 = self.get_cell(position - 1).get_top() if position != 0 else 0
            self.__cell_pillar.insert(position, c.Cell(z0,z0 + size))
            self.__number_of_cells += 1
            for i in range(position + 1, self.__number_of_cells):
                old_z0 = self.get_cell(i).get_bottom()
                old_z1 = self.get_cell(i).get_top()
                self.get_cell(i).set_bottom(old_z0 + size)
                self.get_cell(i).set_top(old_z1 + size)
        else:
            print('wrong position while inserting')

    #информация о клеточном столбе
    def info(self):
        print('\ncell type=', self.__type)
        print('number of cells=', self.__number_of_cells)
        for i in range(self.__number_of_cells):
            print(i)
            print(self.__cell_pillar[i].info())
            print('|–––––––––––––––––|')