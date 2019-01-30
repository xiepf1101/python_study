#coding=utf-8
#svm 支持向量机
import sys
print(sys.path)
sys.path[0] = 'E:\Python\Anaconda\Lib\site-packages'
from sklearn import svm

x = [[2, 0], [1, 1], [2, 3]]
y = [0, 0, 1]

clf = svm.SVC(kernel = 'linear')
clf.fit(x, y)

print(clf)

print(clf.support_vectors_)

print(clf.support_)

print(clf.n_support_)

z = [[2, 0]]
print(clf.predict(z))