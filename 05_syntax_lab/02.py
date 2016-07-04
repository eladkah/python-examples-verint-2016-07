from random import randint

sum = 0
for i in range(0,7):
    sum += randint(1,100)
print 'Sum of 7 random numbers is:', sum
if (sum % 7 == 0):
    print 'Boom'