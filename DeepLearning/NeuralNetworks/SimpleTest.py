#coding=utf-8

from NeuralNetwork import NeuralNetwork
import sys
sys.path[0] = 'E:\Python\Anaconda\Lib\site-packages'
import numpy as np

nn = NeuralNetwork([2,2,1], 'tanh')
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
nn.fit(X, y)
for i in [[0,0], [0,1], [1,0], [1,1]]:
    print(i, nn.predict(i))