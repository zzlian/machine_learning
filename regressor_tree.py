from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing
import pickle

#导入数据集
f = open(r"C:\Users\lenovo\Desktop\电量\datas.pik","rb")
datas = pickle.load(f)
f.close()

#导入数据集对应的label
f = open(r"C:\Users\lenovo\Desktop\电量\label.pik","rb")
label = pickle.load(f)
f.close()

#数据预处理，将特征值范围进行压缩
#datas = preprocessing.scale(datas)
#label = preprocessing.scale(label)

regressor = DecisionTreeRegressor(random_state=0)   #导入回归树
regressor.fit(datas[:-3],label[:-3])    #训练树

#score = regressor.score(datas[-3:],label[-3:])     #获取回归的评分

print(regressor.predict(datas[-3:]))   #进行预测
print(label[-3:])


