import pandas as pd 

salary = pd.Series([20, 15, 18, 30])
score = pd.Series([76, 80, 90, 60], index = ['KOR', 'Math', 'ENG', 'SCI'])
salary
score

score.iloc[0] = 85
score
score.loc['SOC'] = 65
score
score.loc[['ENG', 'Math']] = [70,80]
score

score.loc['PHY'] = 50
score

score.iloc[5] = 90
score

new = pd.Series({'MUS':95})
score = score._append(new)
score

salary._append(pd.Series([66]), ignore_index = True)
salary