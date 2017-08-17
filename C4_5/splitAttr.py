from math import log

def inforEnt(dataSet):
    """计算获取数据的信息熵"""

    counts = {}
    #记录标签对应数据个数
    for data in dataSet:
        label = data[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1

    #计算信息熵
    entropy = 0.0
    for count in counts:
        prob = count / len(dataSet)
        entropy -= prob *  log(prob,2)
    return entropy


def inforGain(dataSet, attributes):
    """获得所有属性的划分信息熵"""
    attrIndex = 0
    inforEnts = []

    for attr in attributes:
        attrValues = []
        for data in dataSet:   #保存数据中对应属性的值
            if data[attrIndex] not in attrValues:
                attrValues.append(data[attrIndex])
        for attrValue in attrValues:
            inforEnts[attrIndex] = 0.0
            datas = []
            for data in dataSet:   #保存每个属性值对应的数据
                if data[attrIndex] == attrValue:
                    datas.append(data)
            inforEnts[attrIndex] += inforEnt(datas) * (len(datas) / len(dataSet))  #获取数据集的信息熵
        attrIndex += 1
    return inforEnts


def splitAttr(inforEnts):
    """由获取的所有属性的划分信息熵获取最小信息熵对应的索引"""

    attrIndex = 0
    minEnt = 0.0
    index = 0
    for ent in inforEnts:
        if minEnt > ent:
            minEnt = ent
            attrIndex = index
        index += 1
    return attrIndex