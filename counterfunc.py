def counter(word, char):
    count = 0   #All variables must be inside the function
    word = str(word)
    for c in word:
        if c == str(char):
            count += 1
    print('Count is : ', count)
word = input('Enter a word: ')
char = input('Enter a char to count: ')
counter(word, char)

#using a built-in count function instead
cnt = word.count(str(char))
print(cnt)