#coding=utf-8
#多元线性回归
import sys
sys.path[0] = 'E:\Python\Anaconda\Lib\site-packages'
from numpy import genfromtxt
import numpy as np
from sklearn import datasets,linear_model

dataPath = r"E:/Python/workspace/DeepLearning/NeuralNetworks/contact - 副本.csv"
deliveryData = genfromtxt(dataPath, delimiter=',')

#print("data",deliveryData)

X = deliveryData[:, :-1]
Y = deliveryData[:, -1]

print("X:\n",X)
print("Y:\n",Y)

regr = linear_model.LinearRegression()

regr.fit(X, Y)

print("coefficients:\n", regr.coef_)
print("intercept:\n", regr.intercept_)

xPred = [[102, 6, 0, 1, 0]]
yPred = regr.predict(xPred)
print("predicted y:",yPred)