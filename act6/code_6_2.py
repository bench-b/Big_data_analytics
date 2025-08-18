import pandas as pd
import matplotlib.pyplot as plt

# Data Preparation
df = pd.read_csv('../data/iris.csv')
dict = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = list(dict[key] for key in df.Species)
# colors = [dict[key] for key in df.Species]
colors

df.plot.scatter (x= 'Petal_Length',
    y= 'Petal_Width',
    s=30,
    c=colors,
    marker='o',)
plt.show()