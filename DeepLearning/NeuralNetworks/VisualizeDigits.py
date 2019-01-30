#coding=utf-8
import sys
sys.path[0] = 'E:\Python\Anaconda\Lib\site-packages'
from sklearn.datasets import load_digits

digits = load_digits()
print(digits.data.shape)

import pylab as pl
pl.gray()
pl.matshow(digits.images[0])
pl.show()


#价格预测
import numpy as np

def fitSLR(x, y):
    n = len(x)
    dinominator = 0
    numerator = 0
    for i in range(0, n):
        numerator += (x[i] - np.mean(x))*(y[i] - np.mean(y))
        dinominator += (x[i] - np.mean(x))**2
    
    print("numerator:",numerator)
    print("dinaminator",dinominator)
    b1 = numerator/float(dinominator)
    b0 = np.mean(y)/float(np.mean(x))
    
    return b0,b1

def predict(x, b0, b1):
    return b0 + x*b1
x = [1, 3, 2, 1, 3]
y = [14, 24, 18, 17, 27]
b0, b1 = fitSLR(x, y)

print("intercept:",b0)
print("slope:",b1)

x_test = 6

y_test = predict(6, b0, b1)

print("y_test:",y_test)
    