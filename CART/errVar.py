from numpy import *

def errVar(y, yHat):
    """返回预测差值的总方差"""
    y = mat(y); yHat =  mat(yHat)
    err = y - yHat      #计算预测值和真实值的差值
    return err*err.T        #返回总方差