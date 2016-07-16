'''
prints all 3 small english letters combinations
'''

small_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print [a+b+c for a in small_letters for b in small_letters for c in small_letters]