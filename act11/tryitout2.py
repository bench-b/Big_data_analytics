import pandas as pd 
import seaborn as sns
from scipy import stats

df = sns.load_dataset('titanic')
df.head()
result = df.pivot_table(index="pclass",
                        columns="alive",
                        values = "alone",
                        aggfunc = "count")
result
survivor_group = result['yes']
death_group = result['no']

stats.chi2_contingency([survivor_group, death_group])