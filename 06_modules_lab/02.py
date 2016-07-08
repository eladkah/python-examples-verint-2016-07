'''
Receives 2 numbers as script parameters and prints their sum.
Usage: python 02.py <number1> <number2>
'''

import sys

num1, num2 = (int(sys.argv[1]), int(sys.argv[2]))
print '%d+%d=%d' % (num1, num2, num1+num2)

