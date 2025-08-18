import pandas as pd 

df = pd.read_csv('../data/iris.csv')
df  #read csv file and display the dataframe

df.info() #General information about dataframe
df.shape #Array shape
df.shape[0] #Number of rows
df.shape[1] #Number of columns


df.dtypes #Data types of each column.  Default type of string is object
df['Species'] = df['Species'].astype('category') #Convert Species column to category type
#It's good to specify it on category because it saves memory, logical ordering, categorical info transfer

df.columns #View column names
df.head() #View part of beginning data
df.tail() #View part of ending data
df['Species'].unique() #Remove duplicate values from data and check unique values

df.iloc[2, 3] #Values in row 2 and columns 3
df.loc[3, 'Petal_Width'] #3rd row value column 'Petal_WIdth'

df.loc[[0, 2, 6], ['Petal_Length', 'Petal_Width']] #Multiple rows and columns specify enclosing []
df.loc[5:8, ['Petal_Length', 'Petal_Width']] #Slicing rows 5 to 8 and columns 'Petal_Length' and 'Petal_Width'

df.iloc[:5, :4]#Values for rows 0-4 and columns 0-3
df.loc[:, 'Petal_Length'] #Formal Expression #All values on 'Petal_Length' column
df['Petal_Length']#Shorthand notation #All values on 'Petal_Length' row

df.iloc[:5, :] #Formal expression #Values of all columns in rows 0-4 
df.iloc[:5]#Shorthand notation #Values of all columns in rows 0-4

#Conditional Statement 
df.loc[df.Petal_Length >= 6.5, :] #to show columnn of rows with Petal_length >= 6.5
df.loc[df.Petal_Length >= 6.5]#same as line 35
df.loc[df.Petal_Length >= 6.5].index #Index of rows with Petal_length >= 6.5

#Conditional Statement 
df.loc[(df.Petal_Length >= 3.5) & (df.Petal_Length <= 3.8)] #this condition shows all the columns but limited on the condition
df.loc[(df.Petal_Length >= 3.5) & (df.Petal_Length <= 3.8), ['Petal_Length']] #this condition shows only the columns for Petal_Length 
df.loc[(df.Petal_Length >=3.5) & (df.Petal_Length <= 3.8), df.columns != 'Species']#this condition exclude the species column but the remaining was included 
df.loc[(df.Petal_Length < 1.3) | (df.Petal_Length > 6.5), ['Petal_Length', 'Petal_Width']] #this condition shows only the columns for Petal_Length and Petal_Width

#Conditional Statement using where
df.where(df.Petal_Length >= 6.5).dropna() #to show columnn of rows with Petal_length >= 6.5

df.loc[:, df.columns != 'Species'] #Exclude Species column
df.loc[:, ~df.columns.isin(['Species'])] #Another method toExclude Species column

df.loc[:, df.columns != 'Species'] + 10 #Add 10 to all columns except Species column

df['Sepal_Length'] + df['Petal_Length'] #Add Sepal_Length and Petal_Length

tmp = df['Petal_Length'].apply(lambda x: -1 if x >= 5 else 1)
df['Petal_Length'] * tmp






