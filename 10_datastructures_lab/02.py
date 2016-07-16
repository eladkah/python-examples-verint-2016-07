'''
Receives file with words separated by lines.
Prints anagrams in same line
Usage: 02.py <file_path>
'''

import sys
import os
if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
    print "Usage: %s <file path>" % sys.argv[0]

dictionary = {}
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')
        # sort line and save as string in dict
        sorted_line = ''.join(sorted(line))

        if sorted_line in dictionary:
            dictionary[sorted_line].append(line)
        else:
            dictionary[sorted_line] = [line]

for key in dictionary:
    for val in dictionary[key]:
        sys.stdout.write(val + " ")
    print ''
