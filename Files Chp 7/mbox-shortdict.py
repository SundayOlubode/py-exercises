# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:13:52 2021

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
ddict = {}
sdict = {}
hdict = {}
for line in fhand:
    if line.startswith('From '):
        linelist = line.split()
        sender = linelist[1]
        sdict[sender] = (sdict.get(sender, 0) + 1)
        handle = (sender.split('@'))[-1]
        hdict[handle] = hdict.get(handle, 0) + 1
        day = linelist[2]
        ddict[day] = (ddict.get(day, 0) + 1)
print('Days\n', ddict)
print('Sender\n',sdict)
print('Handles\n', hdict)
#print(sdict.items())
#to find the maximum value for senders in sdict
allval = sdict.values()
maxval = max(allval)
minval = min(allval)
for n, v in sdict.items():
    if v == maxval:
        print('Max item', n,v)