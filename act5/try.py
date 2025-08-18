import pandas as pd
import matplotlib.pyplot as plt

df = pd.Series(['climbing', 'fishing', 'golf', 'swimming', 'climbing', 'climbing','fishing', 'swimming', 'climbing', 'fishing', 'swimming', 'golf'], 
               )


fig, axes = plt.subplots(ncols=2)

df.value_counts().plot(kind='bar', ax=axes[0], rot=30, title='Bar Graph Visualization', color = 'r')
df.value_counts().plot(kind='pie', ax=axes[1], autopct='%1.1f%%', ylabel='', title='Pie Chart Visualization')

plt.show()


# fig.suptitle('Multiple Graph Example', fontsize=20)
# plt.show()

