# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:55:04 2021

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
count = 0
for line in fhand:
    if line.startswith('From'):
        linelist = line.split()
        sender = linelist[1]
        print ('\n',sender)
        count +=1
print('There were', count,'lines in the file with From as the first word')