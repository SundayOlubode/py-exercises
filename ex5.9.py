num = 0
count = 0
total = 0
average = 0
while True:
    num = input('Enter a number: ')
    if num == "done":
        break
    try:
        float(num)
    except:
        continue
    total = total + float(num)
    count = count + 1
    average = total / count
print(total, count, average)
