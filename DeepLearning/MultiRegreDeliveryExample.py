#coding=utf-8
#E:/Python/workspace/DeepLearning/NeuralNetworks/contact.csv
#多元线性回归
import sys
sys.path[0] = 'E:\Python\Anaconda\Lib\site-packages'
from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model
#英里数	次数  时间
dataPath = r"E:/Python/workspace/DeepLearning/NeuralNetworks/contact.csv"
deliveryData = genfromtxt(dataPath, delimiter=',')

print("data:\r",deliveryData)

X = deliveryData[:, :-1]
Y = deliveryData[:, -1]

print("X:\r",X)
print("Y:\r",Y)

regr = linear_model.LinearRegression()

regr.fit(X, Y)

print('coefficients:', regr.coef_)

print("intercept:",regr.intercept_)

xPred = [[102, 6]]
yPred = regr.predict(xPred)
print("predicted y:",yPred)