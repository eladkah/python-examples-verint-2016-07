'''
mysum calcs sum of parameters while ignoring non-int items
mymul calcs mul of parameters while ignoring non-int items
'''


def mysum(*n):
    return sum(i for i in n if type(i) is int)


def mymul(*n):
    mul = 1
    for j in [i for i in n if type(i) is int]:
        mul = mul * j
    return mul


print mysum('a', 'b', 10, 20)
print mymul('a', 'b', 10, 20)
