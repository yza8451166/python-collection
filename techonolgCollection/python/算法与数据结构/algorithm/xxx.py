#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 16:50
# @Author  : xc
# @Site    : 
# @File    : xxx.py
# @Software: PyCharm


# def quickSort(li,left,right):
#     mid=thrift(li,left,right)
#     quickSort(li,left,mid-1)
#     quickSort(li,mid+1,right)
#
#
#
# def thrift(li,left,right):
#     tmp=li[left]
#     while left<right:
#         while left<right and li[right]>=tmp:
#             right-=1
#         li[left]=li[right]
#         while left<right and li[left]<=tmp:
#             left+=1
#         li[right]=li[left]
#     li[left]=tmp
#     return left


def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[i]
    while j < high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp
li = [3, 51, 8, 2, 5, 22, 13]

def heap(li, low, high):
    n = len(li)

    for i in range(n // 2 - 1, -1, -1):
        sift(li, i, n - 1)

    for i in range(n-1,-1,-1):
        li[0], li[i]=li[i],li[0]
        sift(li,0,i-1)


heap(li,0,len(li)-1)
print(li)