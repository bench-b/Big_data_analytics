import pandas as pd
import matplotlib.pyplot as plt

from pandas.api.types import CategoricalDtype

df = pd.read_csv('../data/BostonHousing.csv')
df = df[['crim', 'rm', 'dis', 'tax', 'medv']]
df

titles = ['crime rate', 'number of rooms',
          'average distamce', 'property tax',
          'housing price']

grp = pd.Series(['M' for i in range(len(df))])
grp.loc[df.medv >= 25] = 'H'
grp.loc[df.medv<= 17.0] = 'L'
df['grp'] =grp
df


new_odr = ['H', 'M', 'L']
new_dtype = CategoricalDtype(categories=new_odr, 
                       ordered=True)

df.grp = df.grp.astype(new_dtype)
df.grp.dtype

df.shape
df.head()
df.dtypes

fig, axes = plt.subplots(nrows = 2, ncols = 3)
fig.subplots_adjust(hspace = 0.5, wspace=0.3)

for i in range(5):
    df[df.columns[i]].plot.hist(ax = axes[i//3, i%3], 
                                ylabel = "", xlabel = titles[i])
fig.suptitle('Histogram Example', fontsize = 14)
fig.show()


fig, axes = plt.subplots(nrows=2, ncols=3)
fig.subplots_adjust(hspace=0.5, wspace=0.3)

for i in range(5):
    df.boxplot(column = df.columns[i], by = 'grp', grid = 'False', ax = axes[i//3, i%3], 
               xlabel = titles[i])
fig.suptitle('Boxplot by group', fontsize=14)
fig.show