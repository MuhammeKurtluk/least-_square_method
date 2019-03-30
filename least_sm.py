
import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)


DF = open('gunesli_saat.txt')
X = DF.readlines()
DF2 = open('satis.txt')
Y = DF2.readlines()

X = [int(i) for i in X]
Y = [int(i) for i in Y]

X_dizi = np.array(X)
Y_dizi = np.array(Y)


x_tpl = X_dizi.sum()
y_tpl = Y_dizi.sum()
xy = X_dizi*Y_dizi
xy = np.array(xy)
x_kare = X_dizi*X_dizi
x_kare = np.array(x_kare)
xy = xy.sum()
x_kare = x_kare.sum()

m = (len(X_dizi)*xy-x_tpl*y_tpl)/(len(X_dizi)*x_kare-pow(x_tpl,2))
b = (y_tpl-m*x_tpl)/len(X_dizi)


Y_tr = m*X_dizi + b

plt.scatter(X_dizi, Y)

plt.plot([min(X), max(X)], [min(Y_tr), max(Y_tr)], color='red')
plt.show()
