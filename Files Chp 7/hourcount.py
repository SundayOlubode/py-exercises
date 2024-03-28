# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 08:30:11 2021

@author: user
"""

#mbox-short.txt
while True:
    fname = input('Enter the filename: ')
    try:
        fhand = open(fname)
        break
    except:
        print('Enter the correct filename')
        continue
hourlist = []
for line in fhand:
    if line.startswith('From '):
        time = line.split()[5]
        hour = time.split(':')[0]
        hourlist.append(hour)
hdict = {}
ttl = []
for h in hourlist:
    hdict[h] = hdict.get(h,0) + 1
for h , n in hdict.items():
    tt = (h, n)
    ttl.append(tt)
    ttl.sort()
for i in ttl:
    print (i)