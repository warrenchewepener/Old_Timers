# Import all the necessary libraries 

import random
import numpy as np
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 


# Create a function and call out "Nearest" and "kluster"
def createclusterdata(Nearest,kluster):

# The number 42 from The Hitchhikers guide to the Galaxy  
    random.seed(42) 
    pointsPerCluster = float(Nearest/kluster)

# Create an empty list      
    Z = [] 


# for Loop in kluster
    for i in range (kluster):

# Two variables on income and age         
        income = random.uniform(50000.0,500000.0)
        age = random.uniform(15.0,80.0) 

# For loop in "pointsPerCluster"
        for j in range(int(pointsPerCluster)):


# spread of data is around 5.0
            Z.append([np.random.normal(income,10000.0),np.random.normal(age,5.0)])

# Create a List where Z was an empty list 
    Z = np.array(Z)
    return Z         


# Pull out a parameter of the value of 100 and clustering of 5 
data = createclusterdata(100,5)

# Clustering of 5 
model =KMeans(n_clusters = 5)
model = model.fit(scale(data))
print(model.labels_)


# plot the figure to 5 inches wide and 6 inches high
plt.figure(figsize=(8,6))

plt.scatter(data[:,0],data[:,1], c = model.labels_.astype(float))

# Plot the graph

plt.show()


