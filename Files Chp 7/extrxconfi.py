# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:17:12 2021

@author: user
"""
conval = 0
linecount = 0
fname = input('Enter the txt file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        line.rstrip()
        lineind = line.find(' ') # i used space after checking the txt file
        conval = float(line[(lineind) : ])
        conval += conval
        linecount += 1
avg = conval/linecount
print('Nos of lines = ', linecount, '\nAverage conval = ', avg)