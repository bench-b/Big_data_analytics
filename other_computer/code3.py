import pandas as pd

score_1 = pd.Series([85, 75, 90], index = ['KOR', 'ENG', 'MATH'])
score_2 = score_1
score_2.loc['KOR'] = 95
score_2
score_1

