# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:08:04 2021

@author: user
"""

import urllib.request as ur
img = ur.urlopen('http://data.pr4e.org/cover3.jpg')
file = open('cover2.jpg', 'wb')

while True:
    detl = img.read(10000)
    if len(detl) < 1: break
    file.write(detl)
file.close()
