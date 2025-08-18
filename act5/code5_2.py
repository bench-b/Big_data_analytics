import pandas as pd
import matplotlib.pyplot as plt

# # Data Preparation
# df = pd.read_csv('../data/cars.csv')
# dist = df['dist']  # braking distance column only dist

# dist.plot.box(title = 'Braking DIstance', color = 'green')
# plt.show()



# Data Preparation
df = pd.read_csv('../data/iris.csv')


df.boxplot(column = 'Petal_Length', 
           by = 'Species',
           grid= True)

plt.suptitle('')
plt.show()

import seaborn as sns
plt.figure(figsize=(6,4))
sns.boxplot(data=df, showFilters = False)
sns.stripplot(data=df, color='black ', alpha=0.5)
plt.show()

