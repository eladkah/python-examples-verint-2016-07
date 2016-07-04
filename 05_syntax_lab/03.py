from random import randint

sum = 0
rand = randint(1,10000)
original = rand
while (rand > 0):
    sum += rand % 10
    rand /= 10
print 'Rand:', original, " sum of digits:", sum