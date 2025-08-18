import pandas as pd
import matplotlib.pyplot as plt

late = pd.Series([5, 8, 7, 9, 4, 6, 12, 13, 8, 6, 6, 4], 
                 index= list (range (1, 13)))

late.plot(title='Late Student per month', #title
          xlabel= 'month', #x axis label
          ylabel= 'frequency', #y axis label
          linestyle = 'dotted', marker='*') #grid
plt.show()

late1 = [5,8,7,9,4,6,12,13,8,6,6,4]
late2 = [4,6,5,8,7,8,10,11,6,5,7,3]

dict ={'Class 1':late1, 'Class 2':late2}
late = pd.DataFrame(dict, index = list(range(1,13)))
late.plot(title='Late Student per month', #title
          xlabel= 'month', #x axis label
          ylabel= 'frequency', #y axis label
          linestyle = 'dotted', marker='*') #grid
plt.show()