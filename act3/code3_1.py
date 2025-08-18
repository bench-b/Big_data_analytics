import pandas as pd 
import numpy as np

temp = pd.Series([-0.8, 0.1, 7.7, 13.8, 18.0, 22.4,
                  25.9, 25.3, 21.0, 14.0, 9.6, -1.4])

temp

temp.index = ['Jan', 'Feb', 'Mar', 'Apr',
              'May', 'Jun', 'Jul', 'Aug',
              'Sep', 'Oct', 'Nov', 'Dec']
temp

#This 3 are Look the same output for checking the tinformation about series objects
temp.size
len(temp)
temp.shape

#This part are for Indexing and slicing 
#Indexing points the location of value stored in the series
#Slicing extracts value from series by using index and conditional statements
#Additional info for .loc[] method only the index label can be used like the Jan up to Dec
temp.iloc[2]
temp.loc['Mar']
temp.iloc[[3, 5, 7]]
temp.loc[['Apr', 'Jun', 'Aug']]
temp.iloc[5:8] #values including start which is 5 but excluding 8 which it ends only 7
temp.loc['Jun': 'Aug'] #values including both start and ends
temp.iloc[:3] #values index 0 up to 3
temp.iloc[4:] #valus index 9 up to end 
temp.iloc[:] #values of all index


#When slicing using conditional statement we must use .loc[] method
temp.loc[temp > 15]
temp.loc[(temp > 15) & (temp < 20)]# condition greater than 15 AND must be less than 20
temp.loc[(temp < 5)| (temp >= 25)]  # condition less than 5 OR greater than or equal to 25
march = temp.loc['Mar'] #just like we created variable name march
march #and this where we print the variable name
temp.loc[temp < march] #it display the less than value of march

#condition search using where 
temp.where(temp >= 15) # it display all the values but for those not 
                    #on greater than equal 15 it display NaN
temp.where(temp >= 15).dropna() #diplay the true value only which is greater than equal 15

temp.loc[temp >= 15] #Extract values meet the condition
temp.loc[temp >= 15].index #Extract only the indices of value 

#Arithmetic operation on series objects
temp + 1 #Add 1 to all values in the series
2 * temp + 0.1
temp + temp
temp.loc[temp >= 15]+1 #Add 1 to all values that meet the condition


#Statistical method on series objects
temp.sum() #Sum of all values in the series
temp.mean() #Average of all values in the series
temp.median() #Median of all values in the series
temp.max() #Maximum value in the series
temp.min() #Minimum value in the series
temp.std() #Standard deviation of the series
temp.var() #Variance of the series
temp.abs() #Absolute value of the series
temp.describe() #Descriptive statistics of the series


