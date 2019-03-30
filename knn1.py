
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data

data = open('gunesli_saat.txt')
X = data.readlines()
data2 = open('satis.txt')
Y = data2.readlines()

X = [int(i) for i in X]
Y = [int(i) for i in Y]
X_mean = np.array(X)
Y_mean = np.array(Y)

num = 0
den = 0
xy = 0
x_kare = 0

x_tpl = X_mean.sum()
y_tpl = Y_mean.sum()
xy = X_mean*Y_mean
xy = np.array(xy)
x_kare = X_mean*X_mean
x_kare = np.array(x_kare)
xy = xy.sum()
x_kare = x_kare.sum()

m = (len(X_mean)*xy-x_tpl*y_tpl)/(len(X_mean)*x_kare-pow(x_tpl,2))
b = (y_tpl-m*x_tpl)/len(X_mean)

# Making predictions
Y_pred = m*X_mean + b

plt.scatter(X_mean, Y) # actual
# plt.scatter(X, Y_pred, color='red')
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()