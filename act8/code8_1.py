import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df.head()

sns.set_theme(style = "whitegrid", rc = {"figure.figsize": (5, 5)})
sns.set_palette('hls', 12)

sns.barplot(data= df, x= 'day', y ='total_bill', estimator= 'mean', 
            hue = 'day', legend= None)

plt.show()


df2 = df.pivot_table(index='day', columns='sex', values='total_bill',
                    aggfunc='mean', observed= True)

df2

df2.plot.bar(stacked = True)
plt.subplots_adjust(bottom=0.2)
plt.show()