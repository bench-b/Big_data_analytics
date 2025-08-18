import pandas as pd

score_1 = pd.Series([80, 75, 90], 
                    index = ['KOR', 'ENG', 'MATH'])
score_2 = score_1 #score_2 and score_1 are the same object
score_2.loc['KOR'] = 95
score_2
score_1

score_3 = score_1.copy() #score_3 is a copy of score_1
score_3.loc['KOR'] = 87
print(score_3) #only KOR = 87 0n score_3
print(score_1) #score_1 remains unchanged