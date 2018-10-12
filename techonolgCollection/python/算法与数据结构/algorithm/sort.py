#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 10:12
# @Author  : xc
# @Site    : 
# @File    : sort.py
# @Software: PyCharm

# 排序究其根本移动下标，赋最大或最小值
import random
import time


def call_time(func):
    def wrapper(*args, **kwargs):
        t_start = time.time()
        x = func(*args, **kwargs)
        t_end = time.time()
        print("Time cost:", t_end - t_start)
        return x

    return wrapper


@call_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break


# data =list(range(1000))
# random.shuffle(data)
# bubble_sort(data)
# print(data)


@call_time
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < len[min_loc]:
                min_loc = j
        if min_loc != j:
            li[i], li[min_loc] = li[min_loc], li[i]


@call_time
def inset_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        print('j :', j)
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = tmp


# @call_time

def quick_sort_x(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort_x(data, left, mid - 1)
        quick_sort_x(data, mid + 1, right)


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1    #将右边下标移动与中间量对比，移动到比中间量小的值赋值给第一次空出来的位置
        data[left] = data[right]  # 填补左边空出来的
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]  # 填补右边空出来的
    data[left] = tmp
    return left


@call_time
def quick_sort(data):
    return quick_sort_x(data, 0, len(data) - 1)


data = list(range(10))
random.shuffle(data)
quick_sort(data)
print(data)

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp


def _mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _mergesort(li,low, mid)
        _mergesort(li, mid+1, high)
        merge(li, low, mid, high)


@call_time
def shell_sort(li):
    gap = int(len(li) // 2)
    while gap >= 1:
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[i - gap] = tmp
        gap = gap // 2

#
# sys.setrecursionlimit(100000)
# #data = list(range(100000, 0, -1))
# data = []
# for i in range(100000):
#     data.append(random.randint(0,100))
# # data.sort()
# #random.shuffle(data)
# data1 = copy.deepcopy(data)
# data2 = copy.deepcopy(data)
# data3 = copy.deepcopy(data)
# #
# # bubble_sort(data1)
# #quick_sort(data2)
# count_sort(data1, 100)
# # sys_sort(data3)
# #mergesort(data3)
# sys_sort(data3)


# li=[1,4,5,6,2,3,7,8,9]
# merge(li, 0, 3, 8)
# print(li)
#