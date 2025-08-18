import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

beers = [5, 2, 9, 8, 3, 7, 3, 5, 3, 5]
bal = [0.1, 0.03, 0.19, 0.12, 0.04, 0.0095, 0.07,
       0.06, 0.02, 0.05]

dict = {'beers': beers, 'bal': bal}
df = pd.DataFrame(dict)
df
df.plot.scatter(x='beers', y = 'bal', title = 'Beers and Balance')

#calculalting regression line
#beers is independent variable  bal is dependent variable
#use polynomial to have regression line
m, b = np.polyfit(beers, bal, 1)
plt.plot(beers, m * np.array (beers)+ b)
plt.show()

df['beers'].corr(df['bal'])