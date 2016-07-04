from random import randint

while True:
    rand = randint(1,1000000)
    if rand % 7 == 0 and rand % 13 == 0 and rand % 15 == 0:
        print rand
        break