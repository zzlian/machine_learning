from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

def getDatas():
    """获取用电量数据集"""
    f = open(r"C:\Users\lenovo\Desktop\电量\user.txt")
    lines = f.readlines()
    datas = []
    i = 0
    for line in lines:
        line = line.split("\t")
        if i == 0:
            i += 1
            continue
        if i == 49:
            break
        datas.append(float(line[1].strip()))
        i += 1
    return datas


def difference(num,dta):
    """将数据集进行差分处理，使时间序列更加平稳"""
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(111)
    diff = dta.diff(num)
    #diff.plot(ax=ax1)
    return diff

def acfAndPacf(dta):
    """绘出自相关和偏自相关图"""
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(dta, lags=40, ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)

def modelToChoose(dta):
    """获取模型的一些评判指数，选择模型"""
    #arma_mod20 = sm.tsa.ARMA(dta, (0,13)).fit()
    #print(arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic)
    arma_mod30 = sm.tsa.ARMA(dta, (1,0)).fit()
    print(arma_mod30.aic, arma_mod30.bic, arma_mod30.hqic)
    arma_mod40 = sm.tsa.ARMA(dta, (0,1)).fit()
    print(arma_mod40.aic, arma_mod40.bic, arma_mod40.hqic)
    arma_mod50 = sm.tsa.ARMA(dta, (13,0)).fit()
    print(arma_mod50.aic, arma_mod50.bic, arma_mod50.hqic)
    return arma_mod50

def testModel(resid):
    """模型检验"""
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)

def predictDatas(model,dta):
    """时间序列预测，由之前的时间序列预测出后续的时间序列"""
    predict_sunspots = model.predict('2048', '2060', dynamic=True)   #时间序列预测
    print(predict_sunspots.values)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax = dta.ix['2001':].plot(ax=ax)       #绘出已有时间序列的折线图
    predict_sunspots.plot(ax=ax)        #绘出预测时间序列的折线图


dta = getDatas()        #获取时间序列
dta=pd.Series(dta)      #将数据序列化，为每个数据指定一个索引
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2048'))  #将普通索引转化为时间索引
#print(dta.values)
#dta.plot(figsize=(12,8))
#diff = difference(1,dta)
#acfAndPacf(dta)
model = modelToChoose(dta)      #获取对应p、q的模型
predictDatas(model,dta)         #预测后续的时间序列
plt.show()


