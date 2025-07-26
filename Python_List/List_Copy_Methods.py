# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 15:20:53 2025

@author: Sudhir Gaikwad
"""

# list copying ()shallow copy vs deep copy


import copy 

#Simple copy

list1 = [[1,2,3,25,35,66,4,5,6],[45,33,23]]
list2 = list1.copy()

# print(list2)

#Deep Copy

list3 = copy.deepcopy(list1)
list3[1][0] = 1000

print(list1)
print(list3)