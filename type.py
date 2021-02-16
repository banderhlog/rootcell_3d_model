import pandas as pd

centers = pd.read_csv('/Users/sanek/Desktop/NSU/cell_3d_model/Centroid_correct.csv', header= None)
cell_walls = pd.read_csv('/Users/sanek/Desktop/NSU/cell_3d_model/cellwall_length_correct.csv', sep=';', header= None)
print(centers.tail())
print(cell_walls.head())
x, y = [], []
#считывание таблицы координат центров
for i in centers.iterrows():
    x_y = list(map(float,i[1][0].split(';')))
    x.append(x_y[0])
    y.append(x_y[0])
centers['x'] = x
centers['y'] = y
centers = centers.drop(0, axis= 1)
del x
del y
print(centers.tail())

#возвращает словарь вида {сосед: длина границы}
def neighbours(column):
    if 0 <= column <= centers.shape[0] - 1:
        n, m = [], []
        for i in range(cell_walls.shape[1]):
            d = cell_walls.loc[column][i]
            if d != 0 and i != 0 :
                n.append(i)
                m.append(d)
        res = dict(zip(n,m))
        return res