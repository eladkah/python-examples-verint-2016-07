from random import randint
import sys

x = randint(1,10)
y = randint(1,10)
print 'x: ', x, 'y: ', y
for ix in range(1, x+1):
    for iy in range(1, y+1):
        if y * ix == x * iy:
            print y * ix
            sys.exit(0)