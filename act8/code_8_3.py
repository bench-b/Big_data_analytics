import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/seoul_temp.csv')
df.head()

#20231201 = 20231201 - 20230000 //100
df['month'] = (df.Date -20230000) //100
df.head()
df.tail()

sns.set_theme(style='whitegrid', rc= {'figure.figsize':(7,4)})

tmp = df.groupby(['month']).mean()
rank = tmp['AvTemp'].rank() - 1
rank = rank.astype(int).to_list()
#original palette
mycolor = sns.color_palette('bwr', 12)
sns.palplot(mycolor)
plt.show()
#modified palette
mycolor = pd.Series(mycolor)[rank].to_list()
sns.palplot(mycolor)
plt.show()

sns.set_palette('hls', 12)

sns.boxplot(data = df, x= 'month', y= 'AvTemp', hue='month', legend=None, palette=mycolor
            ).set(title='Seoul Temperature')

plt.show(
    
)