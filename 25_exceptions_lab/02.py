'''
Gets a file as a parameter and prints its number of lines
Uses exceptions to tell if no parameters or file does not exist
'''

import sys
import os

try:
    if len(sys.argv) != 2:
        raise Exception('Invalid parameters. Expected %s <file_name>' % sys.argv[0])
    if not os.path.exists(sys.argv[1]):
        raise Exception('Sorry, file: %s not found' % sys.argv[1])
    with open(sys.argv[1], 'r') as f:
        lines = sum(1 for line in f)
        print lines

except Exception as e:
    print e.message
