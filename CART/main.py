from CART.binSplitDataSet import binSplitDataSet
from CART.chooseBestSplit import chooseBestSplit
from CART.createForecast import forecast
from CART.createTree import createTree
from CART.errVar import errVar
from CART.loadDataSet import *
from sklearn.tree import export_graphviz

import numpy as np
from numpy import *


def main():
    fileName = r"C:\Users\lenovo\Desktop\电量\user_0.txt"     #指定数据文件
    dataSet = loadDataSet_2(fileName)       #加载数据集
    dataSet  = array(dataSet,np.float)      #将将加载的数据映射为浮点型
    train_data = dataSet[:-8]       #训练集
    test_data = dataSet[-8:]        #测试集
    print(test_data[:,-1])
    tree = createTree(train_data)       #训练决策树
    #export_graphviz(tree, out_file=r"C:\Users\lenovo\Desktop\tree.dot")    #可视化决策树
    yHat = forecast(tree, test_data)        #预测测试集
    print(yHat.tolist())

if __name__ == '__main__':
    main()



