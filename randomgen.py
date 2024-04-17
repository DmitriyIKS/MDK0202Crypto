import random

print('Random number generator \n')

a = int(input('Select min: '))

b = int(input('Select max: '))

r = random.randint(a, b)

print('Random number: ' + str(r))