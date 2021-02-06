#класс клетки
class Cell:

    #конструктор клетки
    def __init__(self, bottom, top):
        if top > bottom:
            self.__top = top
            self.__bottom = bottom
        else:
            print('Wrong values \n')

    #возвращает координату верха клетки
    def get_top(self):
        return self.__top

    #возвращает координату низа клетки
    def get_bottom(self):
        return self.__bottom

    #устанавливает новую координату низа клетки
    def set_bottom(self, new_bottom):
        if new_bottom >= 0 and new_bottom < self.__top:
            self.__bottom = new_bottom
        else:
            print('Less than zero value or bottom > top\n')

    #устанавливает новую координату верха клетки
    def set_top(self, new_top):
        if new_top > 0 and new_top > self.__bottom:
            self.__top = new_top
        else:
            print('Less than zero value or bottom > top\n')

    #информация о клетке
    def info(self):
        print('bottom= ', self.__bottom)
        print('top=', self.__top)