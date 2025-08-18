import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('../data/airquality.csv')
print(df)

#check the missing values
print(df.size)
pd.isna(df)

#remove rows with missing values
df_cleaned = df.dropna().sum()
print(df_cleaned) #df_cleaned


#Removing outliers using IQR
Q1 = df['Ozone'].quantile(0.25)
Q3 = df['Ozone'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Ozone'] < Q1 - 1.5 * IQR) | (df['Ozone'] > Q3 + 1.5 * IQR)]
print(outliers)


#5 compute monthly average 
monthly_avg = df.groupby('Month')[['Ozone', 'Solar.R', 'Wind', 'Temp']].mean()
print(monthly_avg)

# Plot the monthly averages
monthly_avg.plot(kind='line', marker='o')
plt.title('Monthly Averages of Air Quality Measures')
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.legend(title='Variables')
plt.grid(True)
plt.show()