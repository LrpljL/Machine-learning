#coding=utf-8
#15个样本
#计算经验熵，条件熵，信息增益
from math import log
dataSet=[[0, 0, 0, 0, 'no'],
            [0, 0, 0, 1, 'no'],
            [0, 1, 0, 1, 'yes'],
            [0, 1, 1, 0, 'yes'],
            [0, 0, 0, 0, 'no'],
            [1, 0, 0, 0, 'no'],
            [1, 0, 0, 1, 'no'],
            [1, 1, 1, 1, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [2, 0, 1, 2, 'yes'],
            [2, 0, 1, 1, 'yes'],
            [2, 1, 0, 2, 'yes'],
            [2, 1, 0, 1, 'yes'],
            [2, 0, 0, 0, 'no']]
labels=['年龄','有工作','有自己的房子','信贷情况']

def spilt_dataset(dataSet, labels, index):
    dataset1=dataSet
    dataset_new=[]
    for i in range(len(dataset1)):
        if dataset1[i][index] == 0:
            dataset1[i].remove(dataset1[i][index])
            dataset_new.append(dataset1[i])
            # dataset_new.append(dataSet[i].remove(dataSet[i][2]))
    labels.remove(labels[2])
    return dataset_new,labels
dataset_new , labels_new = spilt_dataset(dataSet,labels,2)
#返回经验熵
def empirical_entropy(dataSet):
    empirical_entropy = 0
    list1=[]   #存储标签类别列表
    for i in range(len(dataSet)):
        list1.append(dataSet[i][-1])
    p={}     #存储概率列表
    for j in list1:
        if j not in p.keys() :
            p[j] = list1.count(j)/len(list1)
    for k in p.values():
        empirical_entropy += -k*log(k,2)
    return empirical_entropy

# Condition entropy
#返回条件熵和信息增益

def Condition_entropy(dataSet,labels):

    p1=[{} for i in range(len(labels))]
    list1=[[] for i in range(len(labels))]
    result_res = [0 for i in range(len(labels))]  # 信息增益
    for j in range(len(labels)):
        for i in range(len(dataSet)):
            list1[j].append(dataSet[i][j])
        for l in list1[j]:
            if l not in p1[j].keys():
                p1[j][l] = list1[j].count(l) / len(list1[j])
    # print(list1,"\n",p1)

        list2 = [[] for i in range(len(p1[j].keys()))]
        for k in p1[j].keys():
            for i in range(len(dataSet)):
                if dataSet[i][j] == k:
                    list2[k].append(dataSet[i][-1])
    # print(list2)
        result=[{} for i in range(len(list2))]
        for i in range(len(list2)):
            for h in list2[i]:
                if h not in result[i].keys():
                    result[i][h] = list2[i].count(h)
    # print(result)

        pij=[{} for i in range(len(list2))]
        result_ij=[0 for i in range(len(result))]   #条件熵
        # print(pij,result_ij)
        for i in range(len(result)):
            for k in result[i].keys():
                pij[i][k] = result[i][k]/sum(result[i].values())
                result_ij[i] += -pij[i][k] * log(pij[i][k], 2)
            result_res[j] += result_ij[i]*p1[j][i]
        result_res[j] = empirical_entropy(dataSet) - result_res[j]

    return result_res

print(dataSet,"\n",labels)
print(empirical_entropy(dataSet))
print(Condition_entropy(dataSet,labels))



#python不允许程序员采用传值还是传引用 python参数传递的方式是传对象引用
"""
实际上，这种方式相当于传值和传引用的一种综合。
如果函数收到的是一个可变对象（比如字典或者列表）的引用，
就能修改对象的原始值——相当于通过“传引用”来传递对象。
如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，
就不能直接修改原始对象——相当于通过“传值”来传递对象。
当人们复制列表或字典时，就复制了对象列表的引用同，如果改变引用的值，则修改了原始的参数。
"""
"""
另一点：对于一般变量，假设想达到引用传递的效果，怎么办呢？
python标准库中并没有提供类似C++中专门的引用或指针的机制，要实现函数内部对传入变量的改动有两种途径：
1、通过函数返回值又一次赋值变量。
2、将变量封装在列表中在传给函数。
"""
#浅拷贝 深拷贝
#浅拷贝只会 拷贝父对象，不会拷贝对象中的子对象
# import copy
# a = [1, 2, 3, 4, ['a', 'b']]  #原始对象
#
# e = a[:] #利用分片操作进行拷贝（浅拷贝）
# b = a  #赋值。传对象的引用
# c = copy.copy(a)  #对象拷贝，浅拷贝
# d = copy.deepcopy(a)  #对象拷贝，深拷贝
#
# a.append(5)  #改动对象a
# a[4].append('c') #改动对象a中的['a', 'b']列表子对象

# print(id(a),id(b),id(c),id(d))
#
# print('a = ', a)   # [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# print('b = ', b)   # 对象引用 [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# print('c = ', c)  #浅拷贝 子列表还是对象引用    [1, 2, 3, 4, ['a', 'b', 'c']]
# print('d = ', d)  #深拷贝 相当于生成一个全新的副本  [1, 2, 3, 4, ['a', 'b']]


#可变对象列表
# dict1={"a":1,"b":2}
# dict2=dict1
# dict1["c"]=3
# print(id(dict1),id(dict2))#497156462216 497156462216
# print(dict1,dict2)
# #可变对象字典
# list1=[1,2,3]
# list2=list1
# list2.append(4)
# list1.remove(2)
# print(id(list2),id(list1))#497156662664 497156662664
# print(list1,list2)
# #赋值后都会生成一个新的对象
# list2=[1,2,3,4]
# print(id(list1),id(list2)) #497156662664 497156624328
# print(list1,list2)

#函数传参，对象引用
# def fff(l):
#     l.append(100)
#     l[2].append('c')
#
#     print("global var ", l)  #全局变量
#
#     return l
#
# a = [1, 2, ['a', 'b'], 3]
# b = fff(a)   #
# print(a)
# b.append(1000)
# print(b)
# print(a)
