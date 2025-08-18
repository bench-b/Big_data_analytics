import pandas as pd 
import numpy as np

df = pd.read_csv('../data/iris.csv')
df
df.iloc[0,1] = pd.NA ; df.iloc[0,2] = pd.NA
df.iloc[1,2] = np.nan ; df.iloc[2,3] = None
df.head()

df.isnull().sum()