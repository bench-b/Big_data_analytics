import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/mtcars.csv')
vars = ['mpg', 'disp', 'drat', 'wt']
pd.plotting.scatter_matrix(df[vars], figsize=(12,12))
# df.plot.scatter(x='wt',
#                 y= 'mpg',
#                 s=50,
#                 c='red',
#                 marker='s',
#                 )
plt.show()