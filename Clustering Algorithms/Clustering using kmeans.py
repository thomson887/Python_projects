# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:09:42 2024

@author: justi
"""

from numpy import unique
from numpy import where
import random
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
# from sklearn.cluster import dbscan

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=random.randint(1, 1000),
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=2,
    random_state=4,
    shuffle = True
    
)

# define the model
kmeans_model = KMeans(n_clusters=5)

# assign each data point to a cluster
kmeans_result = kmeans_model.fit(training_data)

# get all of the unique clusters
kmeans_clusters = unique(kmeans_result)

# plot the K-means clusters
for kmeans_cluster in kmeans_clusters:
    # get data points that fall in this cluster
    index = where(kmeans_result == kmeans_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the DBSCAN plot
pyplot.show()