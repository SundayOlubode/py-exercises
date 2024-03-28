# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:12:37 2021

@author: user
"""

first = ('Sunday', 'Tolu', 'Rhoda', 'Ebunoluwa')
last = ('Olubode', 'Olaiya', 'Oluwaseun', 'Adebayo')
num = (89, 56, 67, 33)
ddict = {}
ddict[first,last] = num
print (ddict)
for first,last in ddict:
    print(ddict[first, last])