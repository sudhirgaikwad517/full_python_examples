# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 16:14:49 2025

@author: Sudhir Gaikwad
"""

# implementing the queue usibng list 


class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self , item):
        self.items.inser(0, item)
    def dequeue(self):
        self.item.pop()
    def size(self):
        return len(self.items)

obj = Queue()

print(obj.isEmpty())
