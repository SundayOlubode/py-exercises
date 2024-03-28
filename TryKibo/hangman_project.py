# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:19:28 2021

@author: user
"""
#----
# Project instructions: https://kiboschool.notion.site/Project-Hangman-e7e41de2fbc2462091bccd9034f83baf
# Team Member 1: [Sunday, Olubode]
# Team Member 2: [Mary, Ogunbiyi]
#----

def start_display():
  print('----------')
  print('|    |')
  print('|    ')
  print('|    ')
  print('|   ')
  print('|   ')
  print('-')

# define a function for a wrong input display
def wrong_input():
  print('\nSorry: you lose')
  print('----------')
  print('|    |')
  print('|    O')
  print('|    ')
  print('|   ')
  print('|   ')
  print('-')

#define a function for display when players loses
def lose_game():
  print('\nSorry: you lose')
  print('----------')
  print('|    |')
  print('|    O')
  print('    \|/')
  print('|    |')
  print('|   / \\')
  print('-')
  print('\nGame Over!')
# setting our secret word
secret_word = ('python')

#start game
print('Let\'s play Hangman!\n')
start_display()

store_word = '' # variable that holds our correct inputs
disp_word = "" #to hold correct inputs to be displayed

right_inp = ['_','_','_','_','_','_', ]

#collect user's input
for i in range(len(secret_word)):
  word = input('Please enter a letter or word: ')
  if word not in secret_word:
    print(word, 'is not in the word')
    wrong_input()
    continue
  else:
    print(word, 'is in the word')
    store_word  += word
    pos = secret_word.find(word)
    if word not in right_inp:
      right_inp[pos] = word
      for w in right_inp:
            disp_word += w
    print(disp_word[-6:]) # this displays the last 6 letters of the variable
    
print('The correct letters you entered were ', right_inp)
if store_word == secret_word:
    print('Congratulation! You won')
else:
    lose_game()