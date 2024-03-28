# Kibo FPWP Final Project
# Author: Sunday Olubode

print('\t\t---------------------- WORD RIDDLE ------------------- ')
print('\t\t------------ You\'re welcome to the game --------------')

username = input('Kindly input your name: ')
print('Welcome, ' + username+"!")
print('-------------------------------\n')
print('INTRO: THIS IS A GAME WHERE YOU REARRANGE MISSPELLED WORDS.')
print('Instruction: All input should be in lowercase')
print('LET\'S GET STARTED')
wordbank = ['size','milk','shape','faith','mouth','legend','camera','kerosene']
misspelled = []
err_count = 0 #holds the number of incorrect attempts
numwon = 0 #holds the number of correct attempts

for i in range(len(wordbank)):
    #to make it possible to split along the spaces
    # i replaced all nonspace between each letter with a whitespace
    misspelled.append(wordbank[i].replace('', ' '))
    misspelled[i] = misspelled[i].split(' ')  #makes each element a list by splitting with along the whitespace
    #print(misspelled)
    misspelled[i].pop() # remove the last element (' ') made by split() function
    misspelled[i].pop(0) #remove the first element also
    misspelled[i].sort() #sorting the list to rearrange the letters
    misspelled[i] = ((' ').join(misspelled[i])).replace(' ', '') #to replace the spaces with nonspace
    
    
for i in range(len(misspelled)):
    print('\nYour word is ---> ',misspelled[i])
    ans = input('Input the right word for the misspelled word above: ')
    if ans == wordbank[i]:
        print('CORRECT!')
        numwon += 1
    else:
        print('INCORRECT!, TRY AGAIN')
        for err_count in range(1):
            print("You've got",(1-err_count),"attempts left for:",misspelled[i])
            ans = input('Input another attempt: ')
            if ans == (wordbank[i]):
                print('CORRECT!')
                numwon += 1
                break
            else:
                print('Incorrect!')
                continue
        print('The correct word is:',(wordbank[i]),'\n')
    if (wordbank[i] == wordbank[-1]):
        print('GAME OVER!\tGAME OVER!!\tGAME OVER!!!')
        print('You had',numwon,'over',len(wordbank))
        if numwon < len(wordbank):
            print('You can do better,', username)