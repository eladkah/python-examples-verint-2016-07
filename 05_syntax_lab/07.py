from random import randint

rand = randint(1,100)

guess = 0
while True:
    guess = int(raw_input())
    if guess == rand:
        print 'You are right!'
        break
    # randomize lie
    lie = randint(0,2)
    if lie == 0:
        large = guess < rand
    else:
        large = guess > rand
        
    if large:
        print 'The number is less than:', guess
    else:
        print 'The number is more than:', guess