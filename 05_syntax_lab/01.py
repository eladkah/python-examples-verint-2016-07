# First number is biggest
max = int(raw_input())
for i in range(0,9):
    currInput = int(raw_input())
    if (max < currInput):
        max = currInput
print 'Largest number is:', max