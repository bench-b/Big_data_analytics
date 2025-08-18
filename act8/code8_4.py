import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/crimeRatesByState2005.csv')
df.head()
sns.set_theme(rc ={'figure.figsize':(7,7)})
#alpha is a level of transparency
sns.scatterplot(data = df, x= 'murder', y= 'burglary', 
                size='population', sizes=(20,4000),
                 hue='state', alpha=0.5, legend=None)
plt.xlim(0, 12)

for i in range (0, df.shape[0]):
    plt.text(x = df.murder[i], y = df.burglary[i], s =df.state[i], 
             horizontalalignment='center', size= 'small', color = 'dimgray')
    
plt.show()