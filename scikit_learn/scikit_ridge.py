from numpy import *
import pickle
from sklearn import linear_model
from matplotlib import pyplot as plt
from sklearn import preprocessing

#导入数据集
f = open(r"C:\Users\lenovo\Desktop\电量\datas.pik","rb")
datas = pickle.load(f)
f.close()

#导入数据集对应的label
f = open(r"C:\Users\lenovo\Desktop\电量\label.pik","rb")
label = pickle.load(f)
f.close()

datas = preprocessing.scale(datas)     #将数据特征范围进行压缩

reg = linear_model.Ridge (alpha = .5)    #导入岭回归模型
reg.fit (datas[:-3],label[:-3])     #训练模型
score = reg.score(datas[-3:],label[-3:],)        #获取模型训练的分数
print(reg.predict(datas[-3:]))
print(label[-3:])
print(score)

#print(list(mat(datas)[9:21,-1:].T),"\n",label[9:21])

#plt.scatter(label[9:21],mat(datas)[9:21,-1:])
#plt.show()