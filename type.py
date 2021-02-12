import pandas as pd

centers = pd.read_csv('/Users/sanek/Desktop/NSU/cell_3d_model/Centroid_correct.csv')
centers = centers[:-1]
#cell_walls = pd.read_excel('/Users/sanek/Desktop/NSU/cell_3d_model/cellwall_length_correct.xls')

x, y = [], []
#считывание таблицы координат центров
for i in centers.iterrows():
    x_y = list(map(float,i[1]['x;y'].split(';')))
    x.append(x_y[0])
    y.append(x_y[0])
centers['x'] = x
centers['y'] = y
centers = centers.drop('x;y', axis= 1)
del x
del y
