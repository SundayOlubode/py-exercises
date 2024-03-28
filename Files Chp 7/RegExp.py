# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:06:17 2021

@author: user
"""

import re
fhand =  open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From: ', line):   #the caret sign matches d begining of a line
        print(line)
        
# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
#then with one or more characters till @
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:.+@', line):
        print(line)
        
#to select strings with a particular pattern7
#\S+ matches as many non space characters
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)
dar = re.findall('\S+o\S+',s)
print(dar)

for line in fhand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
lst = []
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+', line)
    if (x in lst) is False:
        if len(x) == 0:
            continue
        else:
        #try:
         #  len(x) == 0 
        #except:
            lst.append(x)
print(lst,'\n', len(lst))

for line in fhand:
    line = line.rstrip()
    if  re.search('^X\S*: [0-9.]+', line):
        print(line)