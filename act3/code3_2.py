import pandas as pd

salary = pd.Series([20, 15, 18, 30])
score = pd.Series([75, 80, 90,60], 
                   index = ['KOR', 'ENG', 'MATH', 'SOC'])

salary
score

#Changing Values 
score.iloc[0] = 100 #Change the value of index 0
score
score.loc['ENG'] = 90 #Change the value of index 'ENG'
score
score.iloc[[0, 1]] = [100, 100] #change the multiple values using iloc[]
score
score.loc[['KOR', 'ENG']] = [200, 200] #change the multiple values using loc[]
score
# score.iloc[5] = 68  #index occurs out of range error because there is no index 5
# score # this will be error not recommended to use

#When adding value to a series object, use loc[] method instead of iloc[]
# This is because loc[] method can create a new index if it does not exist
score.loc['SCI'] = 85 #Add a new index 'SCI' with value 
score
#Adding a new index to salary series this be use if there's no index or indices in the series
nextidx = salary.size
nextidx
salary.loc[nextidx] = 25 #Add a new index with value
salary

#When adding new value the the end of object, use append() method
#Input Parameter type of _append()_ method is Series object
new = pd.Series({'MUS': 98}) # {key: value} is dictionary format
score = score._append(new)
score

#when adding new value to a series object has not been labeled,
#ignore_index = True is recommended
salary = salary._append(pd.Series([60]), ignore_index = True)
salary


score = score.drop('SOC')
score           #CHANGE THE CONTENS OF THE OBJECT SOC already deleted

#if there's no label index
salary = salary.drop(0)
salary           #CHANGE THE CONTENS OF THE OBJECT 0 already deleted

