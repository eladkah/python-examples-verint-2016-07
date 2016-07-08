'''
Prints 'Hello Python' message x times when x is received as a parameter to the script
Prints usage if
'''
import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    arg = int(sys.argv[1])
    for _ in range(0, arg):
        print 'Hello Python'
else:
    print 'Invalid usage. Usage: python 01.py <Number>'
