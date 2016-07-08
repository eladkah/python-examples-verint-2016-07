'''
Searches in directory recursively for files larger than specific size and asks user if he wants to delete them.
Receives the directory and minimum size of file as script parameters. Uses argparse module to read the parameters.
Usage: python 03.py <directoryPath> <minimumFileSizeInKb>
'''

import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Find big files')
parser.add_argument('directory', metavar='D', help="Root directory to search")
parser.add_argument('minSizeInKb', metavar='S', type=int, help="Minimum file size in Kbytes")
args = parser.parse_args()

directory = args.directory
minSizeInKb = args.minSizeInKb

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
