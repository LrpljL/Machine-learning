#coding=utf-8
#python默认使用ASCII码保存文件，即使是注释中含有中文也不行，需加上上一行注释。
#PCA降维
# 寻找一组最大方差的相互正交的投影方向
# 求解：1.样本中心化
#      2.计算特征之间的协方差矩阵
#      3.对协方差矩阵特征值进行从大到小排序，取前k个特征向量作为投影方向构成投影矩阵
#      4.对原样本进行投影矩阵变换，实现原样本数据降维
import numpy as np
from sklearn.decomposition import PCA
def eigValPct(eigVals,percentage):
    sortArray=np.sort(eigVals) #使用numpy中的sort()对特征值按照从小到大排序
    sortArray=sortArray[-1::-1] #特征值从大到小排序
    arraySum=sum(sortArray) #数据全部的方差arraySum
    tempSum=0
    num=0
    for i in sortArray:
        tempSum+=i
        num+=1
        if tempSum>=arraySum*percentage:
            return num
X = np.array([[-1,2,66,-1], [-2,6,58,-1], [-3,8,45,-2], [1,9,36,1], [2,10,62,1], [3,5,83,2]])  #(6,4):6个样本，4维特征
print(X,"\n",X.shape)
pca = PCA(n_components=1,svd_solver='randomized')   #降到1维
pca.fit(X)                  #训练
newX=pca.fit_transform(X)   #降维后的数据
# PCA(copy=True, n_components=2, whiten=False)
print(pca.explained_variance_ratio_)  #输出贡献率
print(newX)                  #输出降维后的数据


x_mean=np.mean(X,axis=0)
x=X-x_mean   #中心化(该操作很有必要，只有中心化后协方差矩阵的特征值才代表投影后的样本方差)
cov_=np.cov(x,rowvar=False)
eigVals,eigVects=np.linalg.eig(cov_)
print(eigVals)
print(eigVects)
k=eigValPct(eigVals,0.9)
eigValInd=np.argsort(eigVals)  #对特征值eigVals从小到大排序
eigValInd=eigValInd[:-(k+1):-1] #从排好序的特征值，从后往前取k个，这样就实现了特征值的从大到小排列
redEigVects=eigVects[:,eigValInd]   #返回排序后特征值对应的特征向量redEigVects（主成分）
lowDDataMat=x@redEigVects #将原始数据投影到主成分上得到新的低维数据lowDDataMat
reconMat=(lowDDataMat@redEigVects.T)+x_mean   #得到重构数据reconMat
print(lowDDataMat)
print(reconMat)

