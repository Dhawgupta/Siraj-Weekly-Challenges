#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 23:20:42 2017

@author: dawg
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


#import random


X = []
y = []
print "Preparing Dataset.."
with open("/home/dawg/Desktop/challenge_dataset.txt","r") as filestream:
    for line in filestream:
        currentline = line.split(",")
        X.append(float(currentline[0]))
        y.append(float(currentline[1]))
print "Dataset prepared .."        
#X = np.copy(X)
#y = np.copy(y)
# training the data
num_train = len(X)
X = np.reshape(X,(-1,1))
y = np.reshape(y,(-1,1))

print "Making Classifier"
linearfit = LinearRegression()
print "Fitting Data"
linearfit.fit(X,y)
# preparing test data
print "Prepaing test data"
test_indices = np.random.choice(num_train,num_train/10)u
pred = linearfit.predict(X[test_indices])
print "Calculating Loss per sample"
loss = np.sum(pred - y[test_indices])
loss /= (num_train/10)
print "Loss is : %f" %loss
plt.scatter(X,y)
plt.plot(X, linearfit.predict(X.reshape(-1,1)))
plt.show()


