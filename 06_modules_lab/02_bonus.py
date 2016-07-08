'''
Receives 2 numbers as script parameters and prints their sum.
Validates input.
Usage: python 02.py <number1> <number2>
'''

import sys


if len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print '%d+%d=%d' % (num1, num2, num1+num2)
else:
    print 'Invalid usage. Usage: python 02.py <number1> <number2>'
