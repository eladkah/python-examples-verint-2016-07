'''
Calculates the sum of the tens digit of the numbers
'''

def calc(*n):
     return sum(int(str(number)[-2]) for number in n if type(number) is int and number >= 10)

print calc(1120, 220, 140, 1, 'a')