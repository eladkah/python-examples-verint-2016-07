'''
Usage: 01.py <targetFile> <sourceFile>
Appends the content of <sourceFile> to the end of <targetFile>
'''

import sys
import os

if len(sys.argv) != 3 or not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
    print 'Usage: %s <targetFile> <sourceFile>' % sys.argv[0]
    sys.exit(1)

with open(sys.argv[1], 'a') as target_file:
    target_file.write('\n')
    with open (sys.argv[2], 'r') as source_file:
        for line in source_file:
            target_file.write(line)