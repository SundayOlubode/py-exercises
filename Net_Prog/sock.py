# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 05:52:50 2021

@author: user
"""

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
link = 'bGET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'
sock.sendall(link)
count = 0
pic = b''
while True:
    data = sock.recv(550)
    if len(data) < 1: break
    count += 1
    pic = pic + data
sock.close()
pos = pic.find(b'\r\n\r\n')
picpos = pos + 4
picture = open('cover2.jpg', 'wb')
picture.write(pic[picpos:])
picture.close()