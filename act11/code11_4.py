import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/wilcoxon_test.csv')
df.head()
df.mean()
(df['post'] - df['pre']).mean()
fig, axes =plt.subplots(nrows=1, ncols=2,)
df['pre'].plot.box(grid=False, ax=axes[0])
plt.ylim([60,100])
df['post']. plot.box(grid=False, ax=axes[1])
plt.show()

stats.wilcoxon(df['post'], df['pre'])