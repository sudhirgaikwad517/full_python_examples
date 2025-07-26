# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 15:42:40 2025

@author: Sudhir Gaikwad
"""

# Stack Using List 

try :
    class Stack(object):
        def __init__(self):
            self.items = []
        def isEmpty(self):
            return self.items == []
        def push(self , item ):
            self.items.append(item)
        def pop(self):
            return self.items.pop()
        def peek(self):
            return self.items[len(self.items)-1]
        def size(self):
            return len(self.items)
        def display(self):
            return self.items
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.pop()
    print(s.peek())
    result = s.display()
    print(result)
except Exception as e :
        print("Error is" , e)