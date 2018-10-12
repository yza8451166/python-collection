#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 16:00
# @Author  : xc
# @Site    : 
# @File    : heap.py
# @Software: PyCharm
import random

def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:  # 只要没到子树的最后
        if j+1 <= high and data[j] < data[j + 1]: #如果有右孩子且比左孩子大
            j += 1  # 移动下标指向子节点的最大值
        if data[j]>tmp: #目的把孩子来顶替爹的位置，上位的是值，调整的是下标
            data[i] = data[j]  # 将最大值赋给父节点，也就是孩子顶替了父亲的位置，但同时空出了孩子他自身节点的位置
            i = j  # 重复上面操作 向上回溯寻找 ，也就是树状递归，寻找新的父亲节点，孩子成为新父亲
            j = 2 * i + 1 #新的孩子节点
        else:       #肯定会空出来一个父亲节点位置
            break

    data[i] = tmp #最高领导放到父亲位置


def heap_sort(data):
    n =len(data)
    for i in range(n//2-1,-1,-1):
        sift(data,i,n-1)
        #堆搭建好了
    for i in range(n-1,-1,-1): #指向堆的最后
        data[0],data[i]=data[i],data[0]#领导退休，刁民上位
        sift(data,0,i-1) #调整出新领导，但不能包括排在最后的领导，所以要减一
li=[]
def heap_sort2(data):
    n =len(data)
    for i in range(n//2-1,-1,-1):
        sift(data,i,n-1)
        #堆搭建好了

    for i in range(n-1,-1,-1): #指向堆的最后
        print('data[0]:', data[0])
        li.append(data[0])

        # data[i]=data[0]
        data[0]=data[i]
        print('data[i]:',data[i])
        sift(data,0,i-1)



data = list(range(10))
random.shuffle(data)
print(data)
heap_sort2(data)
print(li)


# def texc():
#     for i in range(10 // 2 - 1, -1, -1):
#         print(i)
# texc()