#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 14:04
# @Author  : xc
# @Site    : 
# @File    : testcount.py
# @Software: PyCharm


li = []
# def bin_search(li,value):
#     low=0;
#     high=li.length-1;
#
#     while li[mid]!=value:
#         mid = (low + high) // 2
#         if  li[mid]==value:
#             return mid
#         if li[mid]>value:
#             high=mid-1
#         elif li[mid]<value:
#             low=mid+1
#
#
def bubble_sort(li):

    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        if not exchange:
            break


li = [3, 51, 8, 2, 5, 22, 13]


# def insert_sort(li):
#     for i in range(1, len(li)):
#         tmp = li[i]
#         j = i - 1
#         while j >= 0 and li[j] > tmp:
#             li[j + 1] = li[j]
#             j -= 1
#         li[j + 1] = tmp


def select_sort(li):
    for i in range(len(li) - 1):

        maxindex = i

        for j in range(i+1,len(li)):
            # maxvalue = li[i]
            # maxindex = i
            # maxvalue=li[j-1]
            if li[maxindex] < li[j]:
                # maxvalue = li[j]
                maxindex = j

        li[i], li[maxindex] = li[maxindex], li[i]
def quick_sort_x(li,left,right):
    if left<right:
        mid=partition(li,left,right)
        quick_sort_x(li,left,mid-1)
        quick_sort_x(li,mid+1,right)


def partition(data,left,right):
    tmp=data[left]
    while left< right:
        while left <right and data[right]>=tmp:
            right-=1
        data[left]=data[right]
        while left<right and data[left]<=tmp:
            left+=1
        data[right]=data[left]
    data[left]=tmp
    return left


quick_sort_x(li,0,len(li)-1)
print(li)
