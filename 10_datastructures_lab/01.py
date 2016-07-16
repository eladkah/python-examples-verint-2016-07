'''
Receives machine names in command line and searches them in existing host.txt file in format
<machine1>=<ip1>
<machine_n>=<ip_n>
For each input machine print it's IP or a message that it was not found
'''

import sys

if sys.argv == 1:
    print 'Usage: %s [Machine Names...]' % sys.argv[0]

wanted_machines = sys.argv[1:]
exist_machines = {}

# Read file
with open('hosts.txt', 'r') as f:
    for line in f:
        splitted = line.split('=')
        exist_machines[splitted[0]] = splitted[1].rstrip('\n')

for machine in wanted_machines:
    if exist_machines.has_key(machine):
        print 'Machine: %s IP: %s' % (machine, exist_machines[machine])
    else:
        print 'Machine: %s was not found in hosts file' % machine
