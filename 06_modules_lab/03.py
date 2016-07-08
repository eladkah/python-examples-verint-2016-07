'''
Searches in directory recursively for files larger than specific size and asks user if he wants to delete them.
Receives the directory and minimum size of file as script parameters.
Usage: python 03.py <directoryPath> <minimumFileSizeInKb>
'''

import sys
import os

if len(sys.argv) != 3 or not sys.argv[2].isdigit():
    print 'Usage: python 03.py <directoryPath> <minimumFileSizeInKb>'
    sys.exit(1)

directory = sys.argv[1]
minSizeInKb = int(sys.argv[2])

if not os.path.exists(directory):
    print '%s does not exists' % directory
    sys.exit(1)

for root, dirs, files in os.walk(directory):
    for file in files:
        sizeInKb = os.stat(root + "\\" + file).st_size / 1024.0
        filePath = os.path.join(root, file)
        if sizeInKb >= minSizeInKb:
            print '%s size is: %f. Do you want to delete it? (yes/no)' % (filePath, sizeInKb)
            answer = raw_input()
            while answer not in ('yes', 'no'):
                print 'Please enter yes or no'
                answer = raw_input()
            if answer == 'yes':
                os.remove(filePath)
