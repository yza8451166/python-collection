#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 10:52
# @Author  : xc
# @Site    : 
# @File    : practise.py
# @Software: PyCharm

import random


def count_sort(li, max_num):
    count = [0 for i in range(max_num + 1)]
    for num in li:
        count[num] += 1
    i = 0
    for num, m in enumerate(count):
        for j in range(m):
            li[i] = num
            i += 1


data = []
for i in range(10000):
    data.append(random.randint(0, 100))


# def insert_sort(li):
#     for i in range(1, len(li)):
#         tmp = li[i]
#         j = i - 1
#         print('j :', j)
#         while j >= 0 and li[j] > tmp:  # 要插入的牌与前面手里的牌比较，比要插入的牌大，就将比它大的牌往后移动
#             li[j + 1] = li[j]
#             j = j - 1  # 不断向前移动下标让前面的牌与要插入的牌比较，知道遇到比要插入的牌小就停下来
#         li[j + 1] = tmp
def insert(li, i):
    tmp = li[i]
    j = i - 1
    while j >= 0 and li[j] > tmp:
        li[j + 1] = li[j]
        j = j - 1
    li[j + 1] = tmp


def insert_sort(li):
    for i in range(1, len(li)):
        insert(li, i)


def topkx(li, k):
    tmp = [0 for i in range(k + 1)]
    tmp[0] = li[0]
    for i in range(1, len(li)):
        j = len(tmp) - 1
        while j >= 0 and tmp[j] > li[i]:
            tmp[j + 1] = tmp[j]
            j = j - 1
        tmp[j + 1] = li[i]


def topk(li, k):
    top = li[0:k + 1]
    insert_sort(top)
    for i in range(k+1, len(li)):
        top[k] = li[i]
        insert(top, k)
    return top[:-1]



li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# li=[]
ltmp = li[0:11]


def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:  # 只要没到子树的最后
        if j + 1 <= high and data[j] < data[j + 1]:  # 如果有右孩子且比左孩子大
            j += 1  # 移动下标指向子节点的最大值
        if data[j] > tmp:  # 目的把孩子来顶替爹的位置，上位的是值，调整的是下标
            data[i] = data[j]  # 将最大值赋给父节点，也就是孩子顶替了父亲的位置，但同时空出了孩子他自身节点的位置
            i = j  # 重复上面操作 向上回溯寻找 ，也就是树状递归，寻找新的父亲节点，孩子成为新父亲
            j = 2 * i + 1  # 新的孩子节点
        else:  # 肯定会空出来一个父亲节点位置
            break

    data[i] = tmp  # 最高领导放到父亲位置


# def texc():
# for i in ltmp:
#     print(i)
#     print(len(ltmp))
#
# texc()
# def topn(li, n):
#     heap = li[0:n]
#     for i in range(n // 2 - 1, -1, -1):
#         if li[i] > heap[0]:
#             heap[0] = li[i]
#             sift(heap, i, n - 1)
#     for i in range(n - 1, -1, -1):  # 指向堆的最后
#         heap[0], heap[i] = heap[i], heap[0]  # 领导退休，刁民上位
#         sift(heap, 0, i - 1)
#     return heap
def topn(li, n):
    heap = li[0:n]
    for i in range(n // 2 - 1, -1, -1):
        sift(heap, i, n - 1)
    #遍历
    for i in range(n, len(li)):
        if li[i] < heap[0]:
            heap[0] = li[i]
            sift(heap, 0, n - 1)
    for i in range(n - 1, -1, -1):  # i指向堆的最后
        heap[0], heap[i] = heap[i], heap[0]  # 领导退休，刁民上位
        sift(heap, 0, i - 1)  # 调整出新领导
    return heap



