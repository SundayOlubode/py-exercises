import random
for i in range(10):
    x = random.randint(5, 10)
    print(x)

print('Makin choice from t')
t  = [2, 3, 4, 5]
for i in range(4):
    print(random.choice(t))
