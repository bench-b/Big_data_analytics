import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic

df = sns.load_dataset('titanic')
df.head()

dict1 = {0:'die', 1:'alive'}
dict2 = {'male':'Male', 'female':'Female'}

df = df.replace({'survived': dict1})
df = df.replace({'sex': dict2})
df.head()

#Grapd settings 
props = lambda key:{'color': 'lightgreen' if 'alive' in key else 'yellow'}

#graph
mosaic(data = df.sort_values('sex'), index= ['sex', 'survived'],
       properties= props, axes_label= True, title= 'Survival rate by gender')

plt.show()