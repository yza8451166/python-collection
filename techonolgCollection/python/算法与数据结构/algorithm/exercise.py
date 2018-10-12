#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 14:52
# @Author  : xc
# @Site    : 
# @File    : exercise.py
# @Software: PyCharm


def bin_search_range(data_set, value):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            # print('find it')
            left=mid
            right=mid
            while left>=0 and  data_set[left]==value:
                left-=1
            while right<len(data_set ) and data_set[right]==value:
                right+=1
            return (left+1,right-1)
        elif data_set[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return
