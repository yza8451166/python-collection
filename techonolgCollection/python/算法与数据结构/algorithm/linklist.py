#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 16:57
# @Author  : xc
# @Site    : 
# @File    : linklist.py
# @Software: PyCharm

class Node(object):
    def __init__(self,item):
        self.item=item
        self.next=None
a=Node(10)
a.next=Node(20)
a.next.next=Node(30)
# b=Node(20)
# c=Node(30)
# a.next=b
# b.next=c
# print(a.next.item)
# def traversal(head):
#     curNode=head #临时用指针
#     while curNode is not None:
#         print(curNode.data)
#         curNode=curNode.next


#头插法
def createLinkListR(li):
    l=Node()
    r=l
    for num in li:
        s=Node(num)
        s.next=l.next
        l.next=s
    return l


def createLinkListRTail(li):
    l=Node()
    r=l
    for num in li:
        s=Node(num)
        r.next=s
        r=s

class Node(object):
    def __init__(self,item=None):
        self.item=item
        self.next=None
        self.prior=None
#doublelink insert
# p.next=curNode.next
# curNode.next.prior=p
# p.prior=curNode
# curNode.Next=p
# p=curNode.next
#curNode.next=p.next
#p.next.prior= curNode
#del p


def doubleCreateLInkListR(li):
    l=Node()
    r=l
    for num in li:
        s=Node(num)
        r.next=s
        s.prior=r
        r=s
    return l,r





