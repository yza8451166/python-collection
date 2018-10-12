#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:07
# @Author  : xc
# @Site    : 
# @File    : test2.py
# @Software: PyCharm
import copy

li = [1, 2, 4, 3]
target = 6
max_num = 100


def func1():
    for i in range(len(li)):
        if li[i] > target:
            continue  # 正数
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return (i, j)


def bin_search(data_set, value, low, high):
    # li.sort()
    # low = 0
    # high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            # print('find it')
            return mid
        elif data_set[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return


def func2():
    li2 = copy.deepcopy()
    li2.sort()
    for i in range(len(li2)):
        a = i
        b = bin_search(li2, target - li2[a], i + 1, len(li2) - 1)
        if b:
            return (li.index(li2[a]), li.index(li2[b]))


def func3():
    a = [None for i in range(max_num + 1)]
    for i in range(len(li)):
        a[li[i]] = i
        if a[target - li[i]]!=None:
            return (a[li[i]], a[target - li[i]])
data_dict={} #字典实现
