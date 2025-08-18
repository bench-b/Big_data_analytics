import pandas as pd
import itertools

df = pd.read_csv('../data/iris.csv')
df20 = df.sample(n=20, random_state=123) #random state to restore previos sampling result
df20 #random sampling

stratified = df.groupby('Species').apply(
    lambda x: x.sample(frac =0.2, random_state = 123)
)
stratified #stratified sampling

species = df.Species.unique()
combinations = list(itertools.combinations(species, 2))
combinations #combination