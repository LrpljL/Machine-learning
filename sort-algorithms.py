#coding=utf-8
# list1=[int(i) for i in input().split(",")]
# n=4
# for i in range(n):#循环右移
#     list1.insert(0,list1.pop())
# for i in range(n):#循环左移
#     list1.insert(len(list1),list1[0])
#     list1.remove(list1[0])
"""冒泡排序：最好情况下时间复杂度为O(n)
             最坏情况下时间复杂度为O(n^2)
             平均时间复杂度为O(n^2)
"""
"""快速排序（分治法）:平均时间复杂度为O(nlogn)
           最坏时间复杂度为O(n^2)(基本逆序或顺序的情况)
           最好情况能够均匀划分左右两个子集
"""
# import time
# import numpy as np
# def quick_sort(list1,left,right):
#     if(left<right):
#         low=left
#         high=right
#         temp=list1[low]
#         while(low<high):
#             while((low<high)&(list1[high]>=temp)):
#                 high-=1
#             list1[low]=list1[high]
#             while((low<high)&(list1[low]<=temp)):
#                 low+=1
#             list1[high]=list1[low]
#         list1[low]=temp
#         quick_sort(list1,left,low-1)
#         quick_sort(list1,low+1,right)
#
# # list1=[int(i) for i in input().split(",")]
# list2=np.random.randint(800,size=800)
# curr_time1=time.time()
# quick_sort(list2,0,len(list2)-1)
# print(time.time()-curr_time1)
# # list2=[int(i) for i in input().split(",")]
# list3=np.arange(800)
# curr_time2=time.time()
# quick_sort(list3,0,len(list3)-1)
# print(time.time()-curr_time2)
# print(list2,"\n",list3)
"""
0.04602766036987305s
1.10072922706604s
"""
"""双向冒泡排序算法：在正反两个方向交替扫描，第一趟把关键字最大的元素放在序列的最后面
第二趟把关键字最小的元素放在序列的最前面，如此反复进行
"""
# def double_bubblesort(list1,left,right):
#     if(left<right):
#         for i in range(left,right):
#             if(list1[i]>list1[i+1]):
#                 list1[i],list1[i+1]=list1[i+1],list1[i]
#         for j in reversed(range(left+1,right)):
#                 if (list1[j] < list1[j - 1]):
#                     list1[j],list1[j-1]=list1[j-1],list1[j]
#         right -= 1
#         left += 1
#         double_bubblesort(list1,left,right)
# # list1=[int(i) for i in input().split(",")]
# list1=[i for i in range(100)][-1::-1]
# double_bubblesort(list1,0,len(list1)-1)
# print(list1)
#哈希表实现map
import numpy as np
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size#存放键
        self.data = [None] * self.size#存放键值
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
                        nextslot = self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                           not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
myTree =['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])
str1="abc"
",".join(str1)