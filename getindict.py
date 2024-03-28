# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:02:10 2021

@author: user
"""

words = ('Abrakadabra')
newdict = {}
for word in words:
    newdict[word] = (newdict.get(word, 0) + 1)
print(newdict)