# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:58:27 2021

@author: user
"""
print('\n-------Instruction: The filename is \'words.txt\'-------')
dictkeys = {}
while True:
    fname = input('Enter file name: ')
    try:
        fhand = open(fname)
        break
    except:
        print('Please, input the correct filename as instructed above!')
        continue
for line in fhand:
    wordlist = line.split()
    for word in wordlist:
        dictkeys[word] = None
print('\n',dictkeys)
isstrs = str in dictkeys
print('\n String in Dictionary?: ', isstrs)