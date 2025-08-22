import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

#Data Preparation
df = pd.read_csv('../data/iris.csv')
df = df.drop('Species', axis=1)
df.head()

#Data Standardization
scaler = StandardScaler ()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
df_scaled.head()

#Clustering
model = KMeans(n_clusters=3, n_init=10, random_state=123)
model.fit(df_scaled)

#check clustering results
model.cluster_centers_ #cluster center coordinates
model.labels_ #cluster number each row 
model.inertia_ #cluster evaluation score

#DImension reduction
pca = PCA(n_components=2)
transform = pca.fit_transform(df_scaled) #reduce to 2 dimensions
transform = pd.DataFrame(transform)
transform['cluster'] = model.labels_
transform.head()

#Visualization 
sns.scatterplot(
    data=transform,
    x=0,
    y=1,
    hue='cluster',
    palette='Set2',
    legend=False
)
plt.show()

ks=range(1,10)
inertias = pd.Series([])

for k in ks:
    model = KMeans(n_clusters=k, n_init=10, random_state=123)
    model.fit(df_scaled)
    inertias.loc[k]= model.inertia_

plt.figure(figsize=(7,4))
inertias.plot.line(title='Inertias Score',
                   xlabel='number of clusters, k',
                   ylabel='inertia')
plt.show()

