numlist= []
num = 0
while True:
    num = input('Enter a number to make a list: ')
    if num == 'done':
        print('The list is: ', numlist)
        print('Max value: ', max(numlist))
        print('Min value: ', min(numlist))
        break
        
    try:
        float(num)
    except:
        print('Enter an integer value only!')
        continue
    
    numlist.append(num)
    
