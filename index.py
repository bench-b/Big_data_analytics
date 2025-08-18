import pandas as pd
import numpy as np

temp = np.array([[-0.1, 0.0, -0.1, -0.2],
                      [1.8, 2.0, 1.6, 1.6],
                      [6.4, 6.8, 5.6, 5.9],
                      [12.3, 12.9, 11.5, 11.5],
                      [17.9, 18.5, 17.1, 17.1],
                      [22.2, 22.8, 21.6, 21.5]])

temperature = pd.DataFrame(temp)
temperature
temperature.index = ['January', 'February', 'March', 'April', 'May', 'June']
temperature
temperature.columns = ['City 1', 'City 2', 'City 3', 'City 4']
temperature

#2. Average Temperature in March for City 2 using absolute location index
temperature.iloc[2, 1]

#3. Average Temperature in April for CIty 4 using absolute location index
temperature.iloc[3, 3]

#4 Average Temperature in January for city 3 using label index
temperature.loc['January', 'City 3']

#5 Average Temperature in June for City 1 using label index
temperature.loc['June', 'City 1']