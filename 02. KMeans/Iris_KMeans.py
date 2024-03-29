import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans


names= ['sepal-length', 'sepal-width', 'petal-lenth', 'petal-width', 'species']

dataset=pd.read_csv('..\Data\iris.data',names=names,sep=',')

dataset.head()

X=dataset.iloc[:, 0:4].values

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
print('The three cluster centers are:', kmeans.cluster_centers_)
print('Labels of each data point', kmeans.labels_)

plt.scatter(X[:,0], X[:,1])
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:, 1], s=300, c= 'red')
plt.xlabel("sepal-length")
plt.ylabel("sepal-width")
plt.show()
