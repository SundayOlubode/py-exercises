# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:36:55 2021

@author: user
"""
#words = {}
#import urllib.request
#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand:
#    print(line.decode().strip())
#    wordlist = line.decode().split()
#    for word in wordlist:
#        words[word] = words.get(word, 0) + 1
#print(words)

#nreadinf binary files using urllib
import urllib.request, urllib.parse, urllib.error
#use read() to download the entire content into a variable
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    amout = img.read(100000)
    if len(amout) < 1: break
    size += len(amout)
    fhand.write(amout)
print(size, 'characters copied')
fhand.close()