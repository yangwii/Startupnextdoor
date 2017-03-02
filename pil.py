# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:13:15 2017

@author: yangpengjs
"""

from PIL import Image
from pylab import *
import numpy as np

# image = array(Image.open('test.jpg').convert('L'))
# print image.shape
# print image.flatten().shape
import matplotlib.pyplot as plt

cluster1 = np.random.uniform(0.5, 1.5, (2, 10))
cluster2 = np.random.uniform(3.5, 4.5, (2, 10))

X = np.hstack((cluster1, cluster2)).T

plt.figure()
plt.axis([0, 5, 0, 5])
plt.grid(True)
plt.plot(X[:, 0], X[:, 1], 'k.')
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
plt.plot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 'ro')