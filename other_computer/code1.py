# import numpy as np
# import pandas as pd
 
# temp = pd.Series([-0.8, -0.1, 7.7, 13.8, 18.0, 22.4,
#                   25.9, 25.3, 21.0, 14.0, 9.6, -1.4])
# temp

# temp.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July'
#               , 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# temp
# temp.iloc[3]
# temp.loc['Mar']
# temp.iloc[[3, 5, 7]]
# temp.loc[['Apr', 'June', 'Aug']]

# temp.iloc[5:8]
# temp.loc['June':'Sep']
# temp.iloc[:4]
# temp.iloc[:]

# temp.loc[temp >= 15]
# temp.loc[(temp >= 15) & (temp < 25)]
# temp.loc[(temp < 5) | (temp >= 25)]

# March = temp.loc['Mar']
# March

# #this will save as all null number if false
# temp.where(temp>=15)

# temp.where(temp>=15).dropna()

# temp.loc[temp >= 15].index
# temp + 1
# temp + temp
# temp.loc[temp>=15] + 1

# temp.sum()
# temp.mean()