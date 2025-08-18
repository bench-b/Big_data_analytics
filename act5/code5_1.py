import pandas as pd
import matplotlib.pyplot as plt

# Data Preparation
df = pd.read_csv('../data/cars.csv')
dist = df['dist']  # braking distance column only dist

# Histogram
dist.plot.hist(bins=6, color='green')
plt.title('Braking Distance')
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.show()

# Frequency counts with bins
print(dist.value_counts(bins=6, sort=False))
