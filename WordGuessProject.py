# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 20:32:28 2021

@author: user
"""
print('\t\t---------------------- WORD PUZZLE ------------------- ')
print('\t\t------------== You\'re welcome to the game --------------')
username = ('Kindly input your name: ')
wordbank = ['faith','milk','shape'] #,'size','mouth','monkey','laugh','kerosene']
rrdw = []
lst = []
errorcount = 0
numwon = 0
for i in range(len(wordbank)):
    spdw = tuple(wordbank[i])
    lst.append(list(spdw))
    lst[i].sort()
    rrdw.append(('').join(lst[i]))
    print(lst)
print(rrdw)
    
for i in range(len(rrdw)):
    print('\n The word is ---> ',rrdw[i])
    ans = input('Input the right word for the misspelt word above: ')
    if ans == wordbank[i]:
        print('CORRECT!')
        numwon += 1
    else:
        print('INCORRECT!, TRY AGAIN')
        for errorcount in range(2):
            print("You've got",(2-errorcount),"attempts left")
            ans = input('Input another attempt: ')
            if ans == (wordbank[i]):
                print('CORRECT!')
                numwon += 1
                break
            else:
                continue
    if (wordbank[i] == wordbank[-1]):
        print('GAME OVER!\tGAME OVER!! \tGAME OVER!!!')