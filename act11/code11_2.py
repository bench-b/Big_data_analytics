import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/paired_ttest.csv')

df.head()
df.groupby(['before', 'after']).count()
df.groupby(['before', 'after']).mean()
fig, axes =plt.subplots(nrows=2, ncols=2, figsize=(10, 4))
df['before'].plot.box(grid=False, ax=axes[0])
plt.ylim([60,100])
df['after']. plot.box(grid=False, ax=axes[1])
plt.show()

#Normality test
stats.shapiro(df['after']-df['before'])

#paired t-test
stats.ttest_rel(df['after'], df['before'])
stats