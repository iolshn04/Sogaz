import pandas as pd

df_1 = pd.read_csv('test.csv', encoding='utf-8')


df_1.dropna(inplace=True)
df_1.rename(columns= {' орень': 'Корень'}, inplace=True)
df_1.rename(columns= {'values     ': 'values'}, inplace=True)
df_1.drop('Unnamed: 0', axis=1, inplace=True)
df_1.groupby(['x1', 'x2', 'x3', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3', 'values']).sum().reset_index()
df_2 = pd.DataFrame({'x1':['x1 1'], 'new_columns':'ok'})

df_all = pd.merge(df_1, df_2, how="outer")

df_all.to_csv('new-test.csv')