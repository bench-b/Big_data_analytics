import pandas as pd
import numpy as np

data = [60, 62, 64, 65, 68, 69, 120]
data = pd.Series(data)

data.quantile(0.25)
data.quantile(0.5)
data.quantile(0.75)
data.quantile([0.25, 0.5, 0.75])

data.quantile(np.arange(0, 1, 0.1))
data.describe()