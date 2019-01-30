#coding=utf-8
#最邻近规则KNN分类算法 应用

#指定sklearn 文件路径
import sys
print(sys.path)
sys.path[0] = 'E:\Python\Anaconda\Lib\site-packages'
from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()

#数据集
iris = datasets.load_iris()
#print(iris)

#模板训练
#iris.data 特征数据集   iris.target  特征对应类别
knn.fit(iris.data, iris.target)

#模板验证
predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])

print(predictedLabel)

