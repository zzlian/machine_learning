from numpy import *


def isTree(obj):
    """判断该节点是否为叶子节点"""
    return (type(obj).__name__ == "dict")


def regTreeEval(model, inData):
    """返回叶节点保存的值"""
    return float(model)


def treeForecast(tree, inData, modelEval=regTreeEval):
    """对单个数据进行预测"""
    if not isTree(tree): return modelEval(tree, inData)     #若为叶子节点，返回结果
    if inData[tree["spInd"]] <= tree["spVal"]:   #小于等于分裂值，选择左子树
        if isTree(tree["left"]):    #递归预测
            return treeForecast(tree["left"], inData, modelEval)
        else:       #叶子节点，返回结果
            return modelEval(tree["left"], inData)
    else:       #大于分裂值，选择右子树
        if isTree(tree["right"]):
            return treeForecast(tree["right"], inData, modelEval)
        else:
            return modelEval(tree["right"], inData)


def createForecast(tree, testData, modelEval=regTreeEval):
    """对数据集进行预测"""
    m = len(testData)   #获取数据集个数
    yHat = mat(zeros((m,1)))    #生成m*1的全0矩阵
    for i in range(m):      #循环对每个数据进行预测
        yHat[i,0] = treeForecast(tree, mat(testData[i]), modelEval)
    return yHat





