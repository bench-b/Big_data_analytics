import pandas as pd

df = pd.read_csv('../data/iris.csv')
df
df.info()
df.shape
df.shape[0]
df.shape[1]

df.dtypes
df['Species'] = df['Species'].astype('category')
df.dtypes

df.columns
df.head(10)
df.tail()
df['Species'].unique()

df.iloc[2,3]

#Show me the rows of which(Petal_length < 1.3) | (Petal_length < 1.3))
df.loc[(df.Petal_Length < 1.3) | (df.Petal_Length > 6.5 ), ['Petal_Length', 'Petal_Width']]

df.loc[:, df.columns != 'Species'] 

df.loc[:, df.columns != 'Species'] + 10

df['Sepal_Length'] + df['Petal_Length']

#tmp = df['Petal_Length'].apply(lambda x: -1 x >= 5 else 1)
