from sklearn import tree  # 决策树模型
from sklearn.datasets import load_iris  # 数据集

clf = tree.DecisionTreeClassifier()     #导入分类决策树模型
iris = load_iris()       #导入数据集
clf = clf.fit(iris.data, iris.target)       #模型训练

tree.export_graphviz(clf,out_file=r"C:\Users\lenovo\Desktop\tree.dot") #生成树的.dot文件
#生成的文件可用graphviz打开，可看到树的结构图