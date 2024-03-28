# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:23:13 2021

@author: user
"""
# file name is 'romeo.txt'
print('Instruction: The filename is \'romeo.txt\'')
while True:
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
    except:
        continue
storelist = []
for line in fhand:
    linelist = line.split()
for word in linelist:
    if word in storelist:
        continue
    else:
        storelist.append(word)
storelist.sort()
print(storelist)