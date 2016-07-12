'''
Usage: 02.py <firstFile> <secondFile> <targetFile>
Alternately writes lines from firstFile and secondFile to targetFile
'''

import sys
import os
import itertools

if len(sys.argv) != 4 or not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
    print 'Usage: %s <firstFile> <secondFile> <targetFile>' % sys.argv[0]
    sys.exit(1)

with open(sys.argv[1], 'r') as first_file:
    with open(sys.argv[2], 'r') as second_file:
        with open(sys.argv[3], 'w') as output_file:
            for line in itertools.izip_longest(first_file, second_file, fillvalue=''):
                for subline in line:
                    if subline:
                        output_file.write(subline.rstrip('\n') + '\n')
