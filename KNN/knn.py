from numpy import *
import operator

def creatDataSet():
    group = array([[1.0,1.2],[1.0,1.0],[0.0,0.0],[0,0.1]])
    labels = ['A','A','B','B']
    return mat(group),labels

group,labels = creatDataSet()
print(group)
print(group[1][0][0][0])
print(labels)
print()

