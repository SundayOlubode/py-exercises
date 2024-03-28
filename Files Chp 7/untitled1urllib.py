# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:22:09 2021

@author: user
"""

import urllib.request as ur
import re
html = ur.urlopen('http://www.facebook.com').read()
links = re.findall(b'href="(http[s]?:.+?)"', html)
for l in links:
    if len(l) < 1 : continue
    print(l.decode())