#coding=utf-8
# import numpy as np
# import matplotlib.pyplot as plt
#绘制散点图
# np.random.seed(100)  #设置随机种子，每次运行产生随机数不变
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# print(x,"\n",y,"\n",colors)
# area = (30 * np.random.rand(N))**2
# print(area)
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)  # s为面积 ，c为颜色序列 ，alpha为透明度
# plt.show()
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
data=load_iris().data
# print(data.shape)  #(150,4)
# plt.scatter(data[:,2],data[:,3],c='r',alpha=0.5)
# plt.show()
X=data[:,2:]
estimator = KMeans(n_clusters=3)  # 构造聚类器
estimator.fit(X)  # 聚类
label_pred = estimator.labels_  # 获取聚类标签
print(label_pred,label_pred.shape)
# 绘制k-means结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()


def distance(vector1,vector2):
    """
    度量距离
    :param vector1:
    :param vector2:
    :return: distance
    """
    return np.sqrt(np.sum(np.power(vector1-vector2,2)))

def centeral_init(dataset,k):
    """
    随机初始化k个聚类中心
    :param dataset:
    :param k:
    :return: k个聚类中心
    """
    x=np.ndim(dataset)
    init_k= np.zeros((k,x))
    for i in range(k):
        index = np.random.randint(0,dataset.shape[0])
        init_k[i,:] = dataset[index,:]
    return init_k
"""
无监督学习算法聚类（k-means）
算法流程：
1.首先确定k（经验值或者通过改变k实验得到准则函数的拐点）
2.在样本中随机初始化k个聚类中心
3.遍历所有样本计算样本距离k个聚类中心的距离，确定每个样本所属的聚类中心，即属于哪一类
4.更新聚类中心（每一类的均值），返回3，直到准则函数值最小（即所有样本距离所属的聚类中心的距离和最小），也就是所有样本所属的聚类中心不再改变
"""
def K_means(dataset,k):
    """
    :param dataset:
    :param k:
    :return:
    """
    numsamples = dataset.shape[0]
    clusterassment = np.mat(np.zeros((numsamples,2))) #存储类别和与聚类中心的距离
    clusterchanged = True  #聚类中心是否变化的标志位
    centroids = centeral_init(dataset,k)
    print(dataset.shape,centroids.shape)
    while clusterchanged:
        clusterchanged=False
        for i in range(numsamples):
            mindist = 100000.0
            minindex = 0

            for j in range(k): #确定每一个sample的类别
                distance1 = distance(dataset[j, :], centroids[j, :])
                if distance1 < mindist:
                    mindist = distance1
                    minindex = j
            if clusterassment[i,0] != minindex:
                clusterchanged = True
                clusterassment[i,:]=minindex,mindist**2
        for l in range(k):
            pointincluster = dataset[np.nonzero(clusterassment[:,0] == l)]
            centroids[l,:] = np.mean(pointincluster,axis=0)
    return centroids,clusterassment



