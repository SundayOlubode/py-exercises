# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:18:25 2021

@author: user
"""
import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    #if  re.search('^X\S*: [0-9.]+', line):
     #   print(line)
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    s = re.findall('^From .*([0-9][0-9]):', line)
    if len(x) > 0:
        print(x)
    if len(s) > 0: print(s)
dtl = ('Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772')

dipo = '1sjsdhgd'
d = re.findall('[^A-Za-z]', dipo)
print(d)