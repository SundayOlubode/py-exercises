# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:04:27 2021

@author: user
"""

print('\n-------Instruction: The filename is \'mbox-short.txt\'-------')
while True:
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
        break
    except:
        print('Please, input the correct filename as instructed above!')
        continue
#rfile = fhand.read()
for line in fhand:
    line = line.upper()
    print(line)
    
def remv(x):
    x.pop()
    x.pop(0)
    return None

lists = [1,2,3,4,56,7]
remv(lists)
