# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 09:19:54 2021

@author: user
"""
import string
while True:
    fname = input('Enter the filename: ')
    try:
        fhand = open(fname)
        break
    except:
        print('Enter the correct filename')
        continue
let_dict = {}
let_list = []
t_list = []
for line in fhand:
    if line.startswith('From '):
        line.rstrip()
        line.lower()
        line = line.translate(line.maketrans('','', string.punctuation))
        line = line.translate(line.maketrans('','', string.digits))
        words = line.split()
        for word in words:
            tw = tuple(word)
            for t in tw:
                let_dict[t] = let_dict.get(t, 0) + 1

for l, n in let_dict.items():
    t = (l, n)
    t_list.append(t)
t_list.sort()#reverse = True)
for t in t_list:
    print (t)