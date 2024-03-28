# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:45:12 2021

@author: user
"""

import urllib.request as ur
while True:
    link = input('Enter the web link: ')
    try:
        html = ur.urlopen('http://'+ link)
        break
    except:
        print('Input a correct link!')
count = 0
while True:
    content = html.read(1000)
    count += len(content)
    print(content.decode())
    if len(content) < 3000:
        continue
    else:
        break