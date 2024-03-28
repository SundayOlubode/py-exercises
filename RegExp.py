# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:06:17 2021

@author: user
"""

import re
fhand =  open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)