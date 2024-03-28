# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:28:35 2021

@author: user
"""
import re
import urllib.request as u
import urllib.parse, urllib.error
face = u.urlopen('https://docs.python.org').read()
vd = re.findall(b'href="(http[s]?:.+?)"', face)
for v in vd:
    if len(v) > 1:
        print(v.decode())
#print(face)
#for line in face:
#    if 