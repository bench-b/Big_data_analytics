import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/iris.csv')

fig, axis = plt.subplots(nrows=2, ncols=2)#allow to make locations 
df['Petal_Length'].plot.hist(ax =axis[0,0],)
df['Petal_Length'].plot.box(ax =axis[0,1])

fd = df['Species'].value_counts()
fd.plot.pie(ax=axis[1,0])
fd.plot.bar(ax=axis[1,1])

fig.suptitle('Multiple Graph Example', fontsize=20)
plt.show()