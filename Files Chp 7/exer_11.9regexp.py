# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:11:48 2021

@author: user
"""
import re
num = 0
word = input('What\'d you like to find a match for?: ')
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if re.search(word, line):
        num += 1
print('There are', num, 'lines that matched \'', word,'\'')
import statistics as s
xlist = []
for line in fhand:
    line = line.strip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        xint = int(x[0])
        xlist.append(xint)
        #print(x,xint,xlist)
        
print('The average is: ', s.mean(xlist))