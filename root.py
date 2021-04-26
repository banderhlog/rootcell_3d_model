import cell_pillar as cp
import cell
import type as type_lib
import random
import itertools
import numpy as np
from scipy.integrate import odeint
from copy import deepcopy


# класс корня
class Root:

    # конструктор – представляет из себя массив клеточных столбов
    def __init__(self, num_of_pillars, pillar_type):
        if num_of_pillars > 0:
            self.__num_of_pillars = num_of_pillars
            self.__pillar_type = pillar_type
            self.__pillars = []
            for i in range(num_of_pillars):
                a = self.__pillar_type[i]
                pillar = cp.CellPillar(a)
                self.__pillars.append(pillar)
        else:
            print('Zero number pillars')

    # возвращает массив клеточных столбов
    def get_pillars(self):
        return self.__pillars

    # возвращает i-тый клеточный столб
    def get_pillar(self, i):
        return self.__pillars[i]

    # возвращает j-тую клетку i-того столба
    def get_cell(self, i, j):
        #print('trying to set i, j', i, j)
        return self.__pillars[i].get_cell(j)

    # возвращает массив типов клеточных столбов
    def get_types(self):
        return self.__pillar_type

    # возвращает структуру, хранящую значения концентрации веществ в клетках
    def get_substance(self):
        substance = []
        for i in self.get_pillars():
            pill_substance = []
            for j in i.get_cell_pillar():
                pill_substance.append(j.get_c())
            substance.append(pill_substance)
        return substance

    # возвращает структуру, с нулевыми концентрациями веществ
    def get_zero_substance(self):
        substance = []
        for i in self.get_pillars():
            pill_substance = []
            for j in i.get_cell_pillar():
                cell_substance = []
                for k in j.get_c():
                    cell_substance.append(0)
                pill_substance.append(cell_substance)
            substance.append(pill_substance)
        return substance

    # устанавливает новые концентрации веществ в корне
    def set_substance(self, new_substance):
        i = 0
        for pil in new_substance:
            j = 0
            for cel in pil:
                #print('i, j, cel')
                #print(i, j, cel)
                self.get_cell(i, j).set_c(cel)
                j += 1
            i += 1

    # сумма концентраций в корне
    def get_sum_substance(self):
        substance = self.get_substance()
        substance = list(itertools.chain(substance))
        print(substance)
        return substance

    # устанавливает параметры i-того клеточного столба
    def set_pillar_cells(self, i, cells):
        #print('cells',cells)
        self.get_pillars()[i].get_cell_pillar().clear()   # удаляем все элементы
        self.get_pillars()[i].set_number_of_cells(len(cells))
        #print('n', self.get_pillars()[i].get_number_of_cells())
        #print('!!!!', len(cells))
        for j in range(len(cells)):
            if j == 0:
                new_cell = cell.Cell(0, cells[0][1])
                self.get_pillars()[i].get_cell_pillar().append(new_cell)
            else:
                new_cell = cell.Cell(cells[j][0], cells[j][1])
                self.get_pillars()[i].get_cell_pillar().append(new_cell)

    # информация о корне
    def info(self):
        for i in self.get_pillars():
            i.info()

    # возвращает массив значений, разбивающий корень
    # на элементарный разрезы
    def elementary_fragmentation(self):
        res = []
        for i in self.get_pillars():
            if i.get_number_of_cells() != 0:
                res.append(i.cell_to_list())
        b = []
        for i in range(len(res)):
            b += list(res[i])  ###
        b = sorted(list(set(b)))
        return b

    # поиск соседей j-той клетки i-того клеточного столба
    def get_neighbours(self, i, j):
        res = {}
        c = self.get_cell(i, j)
        type_of_pillar = self.get_pillar(i).get_type()
        neighbour_pillars_all = type_lib.neighbours(type_of_pillar)
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
            cell_index = []

            for cell_fragment in cell_fragmentation:
                local_pillar = self.get_pillar(neighbour[0] - 1)
                local_cell = local_pillar.get_cell_wh(cell_fragment[0])
                if local_cell not in cell_index and local_cell != -1:
                    cell_index.append(local_cell)
            # print('соседи для',neighbour,'это',cell_index)
            if len(cell_index) != 0:
                res.update({neighbour[0]: cell_index})
        return res

    # поиск соседей j-той клетки i-того клеточного столба фрагмента [a, b]
    def get_fragmet_neighbours(self, i, j, fragment):

        res = {}
        bottom = fragment[0]
        top = fragment[1]
        c = self.get_cell(i, j)
        if c.get_bottom() <= bottom <= c.get_top() and c.get_bottom() <= top <= c.get_top():
            type_of_pillar = self.get_pillar(i).get_type()
            neighbour_pillars_all = type_lib.neighbours(type_of_pillar)
            neighbour_pillars = []

            for n in neighbour_pillars_all:
                if n[0] in self.get_types():
                    neighbour_pillars.append(n)

            for neighbour in neighbour_pillars:
                cell_index = -1
                local_pillar = self.get_pillar(neighbour[0] - 1)
                local_cell = local_pillar.get_cell_wh(bottom)
                if local_cell != -1:
                    cell_index = local_cell
                    res.update({neighbour[0]: cell_index})

        return res

    # обмен веществ между клеточыми столбами
    # прикрутить площадь клеточного столба и коэффициент проницаемости клеточных стенок
    # найти ошибку с обменом между клетками

    def metabolism(self, time):
        root_fragmentation = self.elementary_fragmentation()
        subsctances = self.get_substance()
        # print('old substances',subsctances)
        new_substances = deepcopy(subsctances)
        i = 0
        for p in self.get_pillars():
            j = 0
            for c in p.get_cell_pillar():
                neighbours = self.get_neighbours(i, j)
                # пропускаем, если нет соседей
                if neighbours == {}:
                    continue
                    # есть соседи сверху и снизу

                cell_fragmentation = [c.get_bottom(), c.get_top()]
                for root_fragment in root_fragmentation:
                    if cell_fragmentation[0] < root_fragment < cell_fragmentation[1]:
                        cell_fragmentation.append(root_fragment)
                cell_fragmentation = sorted(cell_fragmentation)
                cell_fragmentation = cp.list_to_cell(cell_fragmentation)
                # print(cell_fragmentation)
                n_cell_fragment = 0

                for cell_fragment in cell_fragmentation:

                    fragment_height = cell_fragment[1] - cell_fragment[0]
                    fragment_neighbours = self.get_fragmet_neighbours(i, j, cell_fragment)
                    # print(i,j,cell_fragment)
                    # print('fragment neighbours', fragment_neighbours)

                    if fragment_neighbours == {}:
                        continue

                    # c_loc - концентрация вещества c в рассматриваемой клетке
                    # c_neigh - массив значений вещества с в соседних к нашей клетке
                    # h - массив длин пятен контакта соседних клеток с нашей
                    # H - массив длин соседних клеток
                    # D - массив коэффициентов диффузии
                    # pillar_square - площадь сечения клеточного столба
                    # v - коэффициент распада вещества с
                    # a - коэффициент синтеха вещества с
                    # i - индекс клеточного столба
                    # j - индек клетки в клеточном столбе
                    # t - обязательный параметр для решателя
                    # top - является ли фрагмент клетки самым верхним
                    # bottom - является ли фрагмент клетки самым нижним
                    # c_bot - вещество с под нашей клеткой
                    # c_top - вещество с над нашей клеткой

                    def dydt(c_loc, t, y0, c_neigh, h, H, D, pillar_square,
                             v, a, i, j, top=False, bottom=False, c_bot=0, c_top=0):

                        c_loc = float(c_loc[0])
                        bot, top1 = 1, 1
                        if bottom == False:
                            bot = 0
                        if top == False:
                            top1 = 0

                        function = 0
                        volume = self.get_cell(i, j).get_length() * pillar_square
                        for i in range(len(H)):
                            function += (c_neigh[i] - c_loc) * h / H[i] * D
                        function = function / volume
                        function += bot * (c_bot - c_loc) * pillar_square * D / volume
                        function += top1 * (c_top - c_loc) * pillar_square * D / volume
                        function = function - v * c_loc * 0 + a * c_loc * 0
                        return function

                    # тут реализовать все массивы данных кроме вещества с
                    top, bottom = False, False
                    if n_cell_fragment == 0 and j != 0:
                        bottom = True
                    '''
                    print('номер фрагмента', n_cell_fragment)
                    print('всего фрагментов', len(cell_fragmentation) - 1)
                    print('j', j)
                    print('всего клеток', p.get_number_of_cells())
                    '''
                    if n_cell_fragment == (len(cell_fragmentation) - 1) and (j + 1) != p.get_number_of_cells():
                        top = True
                    h = fragment_height
                    H = []
                    D = 0.25
                    a = 1.2
                    v = 0.9
                    pp = p.get_type()
                    pillar_square = type_lib.area(pp)

                    for pil, cel in fragment_neighbours.items():
                        # print('pill cell', pil, cel)
                        local_cell = self.get_cell(pil - 1, cel)
                        H_i = local_cell.get_length()
                        H.append(H_i)

                    c_iter = 0
                    for c_loc in c.get_c():

                        # получаем массив c_i соседних клеток
                        c_neigh = []
                        for pil, cel in fragment_neighbours.items():
                            local_cell = self.get_cell(pil - 1, cel)
                            c_neigh.append(local_cell.get_c()[c_iter])
                        c_top, c_bot = 0, 0
                        if top:
                            top_neighbour = self.get_cell(i, j + 1)
                            c_top = top_neighbour.get_c()[c_iter]

                        if bottom:
                            bottom_neighbour = self.get_cell(i, j - 1)
                            c_bot = bottom_neighbour.get_c()[c_iter]

                        # решаем диффур
                        t = np.linspace(0, 10)
                        y0 = subsctances[i][j][c_iter] / len(cell_fragmentation)
                        '''
                        print('y0=', y0)
                        print('t=', t)
                        print('c_loc=', c_loc)
                        print('c_neigh=', c_neigh)
                        print('h=', h)
                        print('H=', H)
                        print('D=', D)
                        print('pillar_square=', pillar_square)
                        print('v=', v)
                        print('a=', a)
                        print('i=', i)
                        print('j=', j)
                        print('top=', top)
                        print('bottom=', bottom)
                        print('c_top', c_top)
                        print('c_bot', c_bot)
                        '''

                        sol = odeint(dydt, y0, t, args=deepcopy((c_loc, c_neigh, h, H, D, pillar_square,
                                                        v, a, i, j, top, bottom, c_bot, c_top)))
                        solution = []
                        for sol_iter in range(len(sol)):
                            solution += list(sol[sol_iter])
                        new_c_i = solution[time]
                        new_substances[i][j][c_iter] = new_c_i
                        # print('выбранное решение', subsctances[i][j][c_iter])
                        # self.set_substance(subsctances)
                        c_iter += 1
                    n_cell_fragment += 1
                j += 1
            i += 1
        self.set_substance(new_substances)
        return subsctances

    # заполнение корня клетками
    def set_root(self, len_of_root, num_of_layers):
        num_of_pils = self.__num_of_pillars
        cells = []
        for i in range(num_of_pils):
            local_cells = [0, len_of_root]
            for j in range(num_of_layers):
                a = random.randint(0, len_of_root)
                # print(a)
                if a not in local_cells:
                    local_cells.append(a)
                else:
                    j = j - 1
            cell_pillar_i = cp.list_to_cell(local_cells)
            cells.append(cell_pillar_i)
        # print('cells',cells)
        for i in range(len(cells)):
            self.set_pillar_cells(i, cells[i])