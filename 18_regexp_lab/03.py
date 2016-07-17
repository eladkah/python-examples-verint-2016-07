'''
Receives csv file and exchange each line first 2 columns
Shana,Sargent,shanasargent@isoswitch.com -> Sargent,Shana,shanasargent@isoswitch.com
'''

import sys
import os
import re


if len(sys.argv) != 2:
    print 'Usage: %s <file_name>' % sys.argv[0]
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print 'Could not find file: %s' % sys.argv[1]
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    for line in f:
        sub = re.sub(r'^(\w*),(\w*)', lambda m: m.group(2) + ',' + m.group(1), line)
        print sub
