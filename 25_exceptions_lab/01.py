'''
Gets numbers as input from user and prints sqrt(number)
If input is not a number or is a negative number, uses exceptions to show error
'''

import math


def try_parse_float(string):
    try:
        return float(string)
    except ValueError:
        raise ValueError('Input \'%s\' is not a number' % string)


def sqrt(n):
    if type(n) == str:
        n = try_parse_float(n)
    if n < 0:
        raise ValueError('Expected positive number, got %f' % n)
    return math.sqrt(n)


while True:
    try:
        arg = raw_input('Please enter a number:')

        res = sqrt(arg)
        print 'Square is %f' % res
    except ValueError as e:
        print 'Error: %s ' % e.message
