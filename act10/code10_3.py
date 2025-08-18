import pandas as pd 
from scipy import stats 
import matplotlib.pyplot as plt

df = pd.read_csv('../data/ind_ttest.csv')

df.head()
df.groupby('group').count()
df.groupby('group').mean()
df.groupby('group').boxplot(grid=False)
plt.show()

group_1 = df.loc[df.group == 'A','height']
group_2 = df.loc[df.group == 'B', 'height']
group_1
group_2

#Normality test
stats.shapiro(group_1)
stats.shapiro(group_2)

stats.ttest_ind(group_1, group_2)