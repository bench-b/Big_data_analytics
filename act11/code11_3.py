import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/mw_test.csv')


df.head()
df.groupby('group').count()
df.groupby('group').mean()
df.groupby('group').boxplot(grid=False)
plt.show()


group_1 = df.loc[df.group == 'A','score']
group_2 = df.loc[df.group == 'B', 'score']
stats.mannwhitneyu(group_1, group_2)