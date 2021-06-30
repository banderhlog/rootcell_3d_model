# класс клетки
import random
class Cell:

    # конструктор клетки
    def __init__(self, bottom, top):
        if top > bottom:
            self.__top = top
            self.__bottom = bottom
            self.__c = [0]*3
            self.__age = 0

            for i in range(len(self.__c)):
                self.__c[i] = random.uniform(0, 1)

        else:
            print('Wrong values \n')

    # возвращает координату верха клетки
    def get_top(self):
        return self.__top

    # возвращает координату низа клетки
    def get_bottom(self):
        return self.__bottom

    # возвращает длину клетки
    def get_length(self):
        return self.__top - self.__bottom

    # устанавливает новую координату низа клетки
    def set_bottom(self, new_bottom):
        if 0 <= new_bottom < self.__top:
            self.__bottom = new_bottom
        else:
            print('Less than zero value or bottom > top\n')

    # устанавливает новую координату верха клетки
    def set_top(self, new_top):
        if new_top > 0 and new_top > self.__bottom:
            self.__top = new_top
        else:
            print('Less than zero value or bottom > top\n')

    # информация о клетке
    def info(self):
        print('bottom= ', self.__bottom)
        print('top=', self.__top)

    # доступ к веществам клетки
    def get_c(self):
        return self.__c

    # доступ к i-ому веществу клетки
    def get_ci(self, i):
        return self.__c[i]

    # установить новые вещества клетки
    def set_c(self, new_c):
        del self.__c
        self.__c = new_c