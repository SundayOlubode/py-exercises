# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 06:03:45 2021

@author: user
"""

import urllib.request as u, urllib.parse, urllib.error
lhand = u.urlopen('http://data.pr4e.org/romeo.txt')
pic = b''
picture = b''
for line in lhand:
    if len(line) < 1:
        break
    picture += line
pfile = open('cover4.jpg', 'wb')
pfile.write(picture)
pfile.close()