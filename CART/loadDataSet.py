def loadDataSet(fileName):
    """读取指定文件中的数据集"""
    dataMat = []
    f = open(fileName)  #读取文件
    for line in f.readlines():
        curLine = line.strip().split("\t")    #将每行进行划分
        fltLine = map(float,curLine)    #将每行映射成浮点数
        dataMat.append(fltLine)
    return dataMat