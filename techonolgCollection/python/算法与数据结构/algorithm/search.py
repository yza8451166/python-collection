#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 9:50
# @Author  : xc
# @Site    : 
# @File    : search.py
# @Software: PyCharm
import time
import random
def call_time(func):
    def wrapper(*args,**kwargs):
        t_start=time.time()
        x=func(*args,**kwargs)
        t_end=time.time()
        print("Time cost:",t_end-t_start)
        return x
    return wrapper



def random_list(n):
    ids=list(range(1001,1001+n))
    a1=['zhao','qian','sun','li']
    a2=['li','hao','','']
    a3=['qiang','guo','jun']
    for i in range(n):
        age =random.randint(18,60)
        id=ids[i]
        name=random.choice(a1)+random.choice(a2)+random.choice(a3)


def linear_search(data_set,value):
    for i in range(range(data_set)):
        if data_set[i] ==value:
            return i
    return
def bin_search(data_set, value):
    low = 0
    high = len(data_set) - 1
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
data = list(range(1000))
bin_search(data, 500)
