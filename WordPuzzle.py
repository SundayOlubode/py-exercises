# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 20:32:28 2021

@author: user
"""
print('\t\t---------------------- WORD PUZZLE ------------------- ')
print('\t\t------------ You\'re welcome to the game --------------')

username = ('Kindly input your name: ')
wordbank = ['faith','milk','shape'] #,'size','mouth','monkey','laugh','kerosene']
spdw=[]
rrdw = []
err_count = 0
numwon = 0
for i in range(len(wordbank)):
    #to make it possible to split-along the spaces
    spdw.append(wordbank[i].replace('', ' '))
    #print(spdw)

for i in range(len(spdw)):
    rrdw.append(spdw[i])
    #print(rrdw)
for i in range(len(spdw)):
    rrdw[i] = spdw[i].split(' ')  #working on elements which are strings
    rrdw[i].pop()
    rrdw[i].pop(0)
    #print (rrdw)
    rrdw[i].sort() #working on list, no assignment needed
    rrdw[i] = ((' ').join(rrdw[i])).replace(' ', '') #to replace the spaces  
for i in range(len(rrdw)):
    print('\n The word is ---> ',rrdw[i])
    ans = input('Input the right word for the misspelt word above: ')
    if ans == wordbank[i]:
        print('CORRECT!')
        numwon += 1
    else:
        print('INCORRECT!, TRY AGAIN')
        for err_count in range(2):
            print("You've got",(2-err_count),"attempts left")
            ans = input('Input another attempt: ')
            if ans == (wordbank[i]):
                print('CORRECT!')
                numwon += 1
                break
            else:
                print('The word is:',(wordbank[i]))
                continue
    if (wordbank[i] == wordbank[-1]):
        print('GAME OVER!\tGAME OVER!! \tGAME OVER!!!')