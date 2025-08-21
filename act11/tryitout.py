import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/prestige.csv')
df.head()

group_1 = df.loc[df.type == 'wc', 'income']
group_2 = df.loc[df.type == 'bc', 'income']
group_1
group_2

group_1.count()
group_2.count()

group_1.mean()
group_2.mean()

stats.shapiro(group_1)
stats.shapiro(group_2)

stats.ttest_ind(group_1, group_2, equal_var=True)



# wc_data = df[df['type'] == 'wc'] 
# wc_data
# bc_data = df[df['type'] == 'bc'] 
# bc_data

# ####2
# wc_sample_size = len(wc_data)
# print("Sample Size for White Collars:", wc_sample_size)
# wc_avg_income = wc_data['income'].mean()
# print("Average Income for White Collars:", wc_avg_income)
# bc_sample_size = len(bc_data)
# print("Sample Size for Blue Collars:", bc_sample_size)
# bc_avg_income = bc_data['income'].mean()
# print("Average Income for Blue Collars:", bc_avg_income)

# ######3
# wc_normality = normality_test()
