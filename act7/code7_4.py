import pandas as pd
import numpy as np
from scipy import stats

#outliers
df = pd.read_csv('../data/iris.csv')
sw= df['Sepal_Width']
#using Z-score
z = np.abs(stats.zscore(sw))
z
outliers = sw[z>2]
print(outliers) #DETECT OUTLIERS using Z-score

Q1 = sw.quantile(0.25)
Q3 = sw.quantile(0.75)
IQR = Q3 - Q1 
IQR #DETECT OUTLIERS using IQR

outliers2 = sw[(sw < Q1 - 1.5 * IQR) | (sw > Q3 + 1.5 * IQR)]
print(outliers2)


clean = sw.loc[~sw.isin(outliers)]
clean[30:41]
