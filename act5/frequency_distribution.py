import pandas as pd
import matplotlib.pyplot as plt

favorite = pd.Series(['WINTER', 'SUMMER', 'SPRING', 'SUMMER',
                     'SUMMER', 'FALL', 'FALL', 'SUMMER', 'SPRING',
                      'SPRING'])
favorite
favorite.value_counts() #calculate frequency distribution
favorite.value_counts() / favorite.size #calculating ratios

fd =favorite.value_counts()
type(fd)
fd['SUMMER']
fd.iloc[2]


#Creating bar graph
#fd is the frequent value of series object
fd.plot.bar(xlabel = 'SEASON',
            ylabel = 'FREQUENCY',
            rot = 45, #rotation angle 0 display horizontally, 45 display 45 degree angle, 90 display vertically
            title = 'FAVORITE SEASON',
            )
plt.show()


fd.plot.barh(xlabel = 'FREQUENCY',
             ylabel = 'SEASON',
             rot =0,
             title = "FAVORITE SEASON")
plt.subplots_adjust(left=0.3)
plt.show()