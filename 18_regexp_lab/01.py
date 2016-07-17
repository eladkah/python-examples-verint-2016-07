'''
Receives a file in format
x1 = y1
x2 = y2
...
and a key (x) and prints the value of x (y)
Uses regex to find relevant line
'''

import sys
import os
import re

if len(sys.argv) != 3:
    print 'Usage: %s <file_name> <key>' % sys.argv[0]
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print 'File: %s does not exist' % sys.argv[1]
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    for line in f:
        result = re.search(r'%s[ ]*=[ ]*(\d*)' % sys.argv[2], line)
        if result:
            print result.group(1)

