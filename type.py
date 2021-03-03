import pandas as pd

centers = pd.read_csv('/Users/sanek/Desktop/NSU/cell_3d_model/Centroid_correct.csv', header= None)
cell_walls = pd.read_csv('/Users/sanek/Desktop/NSU/cell_3d_model/cellwall_length_correct.csv', sep=';', header= None)
#print(centers.tail())
#print(cell_walls.head())
x, y = [], []
#считывание таблицы координат центров
for i in centers.iterrows():
    x_y = list(map(float,i[1][0].split(';')))
    #print(x_y)
    x.append(x_y[0])
    y.append(x_y[1])
centers['x'] = x
centers['y'] = y
centers['cs area'] = [1] * len(x)
centers = centers.drop(0, axis= 1)
del x
del y
print(centers)

#возвращает массив вида (сосед_i: длина границы_i)
def neighbours(column):
    if 0 <= column <= centers.shape[0] - 1:
        n, m = [], []
        for i in range(cell_walls.shape[1]):
            d = cell_walls.loc[column][i]
            if d != 0 and i != 0 :
                n.append(i)
                m.append(d)
        #res = dict(zip(n,m))
        res = list(zip(n,m))
        return res

#протестировать
#возвращает площадь i-того клеточного столба
def area(i):
    return centers.loc['cs area', i]

#возвращает координаты центра i-того клеточного столба
def center(i):
    return [centers.iloc[i, 0], centers.iloc[i, 1]]