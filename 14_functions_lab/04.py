'''
Method that returns the words that are longer than parameter
'''

def longer_than(num, *words):
    return [x for x in words if len(x) > num]

print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')
