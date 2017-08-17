import pickle
#导入数据集
f = open(r"C:\Users\lenovo\Desktop\电量\datas.pik","rb")
datas = pickle.load(f)
f.close()

#导入数据集对应的label
f = open(r"C:\Users\lenovo\Desktop\电量\label.pik","rb")
label = pickle.load(f)
f.close()

f = open(r"C:\Users\lenovo\Desktop\电量\user_0.txt","w")

num = len(label)
for i in range(num):
    line = str(datas[i][0])+"\t"+str(datas[i][1])+"\t"+str(datas[i][2])+"\t"+str(datas[i][3])+"\t"+str(label[i])+"\n"
    f.writelines(line)
f.close()