# Dice roller Generator

import random

print('Enter the choice of input of dice:')
print('a.1 dice')
print('b.2 dice')
print('c.3 dice')
c = input()

if c=='a':
	print('The value on dice is : {}'.format(random.randint(1,7)))
elif c=='b':
	print('The value on dice is : {}'.format(random.randint(1,13)))
elif c=='c':
	print('The value on dice is : {}'.format(random.randint(1,19)))
else:
	print('enter valid input')



