#coding=utf-8
#决策树
import sys
print(sys.path)
sys.path[0] = 'E:\Python\Anaconda\Lib\site-packages'
print(sys.path)
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

header = []
featureList = []
labelList = []
i=0
with open(r'C:\Users\Administrator\Desktop\testData.csv') as csvfile:  
    readCSV = csv.reader(csvfile, delimiter=',')  
    for row in readCSV:  
        if i==0:
            header = row
            i=1
        else:
            rowDict = {}
            labelList.append(row[len(row)-1])
            for j in range(1, len(row) - 1):
                rowDict[header[j]] = row[j]
            featureList.append(rowDict)
        print(row)  
        print(row[0])  
        print(row[0],row[1])    
print(header)
print(labelList)
print(featureList)

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print(dummyX)

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:" + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyX, dummyY)
print("clf:" + str(clf))

with open(r"C:\Users\Administrator\Desktop\allElectronicInfomationGainOri.dot" ,"w") as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file = f)
    
oneRowX = dummyX[0, :]
print("oneRowX: "+str(oneRowX))

newRowX = oneRowX

newRowX[0] = 1
newRowX[2] = 0
print("newRowX : "+str(newRowX))

newRowX = newRowX.reshape(1, -1)  #重塑 reshape(1, -1) 一行n列
print ("newRowx:" + str(newRowX))

#预测
predictedY = clf.predict(newRowX)
print("predictedY: "+str(predictedY))