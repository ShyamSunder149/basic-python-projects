# Random password generator

import random

def shuffle(string):
	tempList = list(string)
	random.shuffle(tempList)
	return ''.join(tempList)

print('Your randomly generated password:')

uppercase1 = chr(random.randint(65,90))
uppercase2 = chr(random.randint(65,90))
number1 = random.randint(0,9)
number2 = random.randint(0,9)
lowercase1 = chr(random.randint(97,122))
lowercase2 = chr(random.randint(97,122))
lowercase3 = chr(random.randint(97,122))
lowercase4 = chr(random.randint(97,122))
s = [35,36,37,38,64]
symbol1 = chr(random.choice(s))
symbol2 = chr(random.choice(s))

password = uppercase1+uppercase2+lowercase1+lowercase2+lowercase3+lowercase4+str(number1)+str(number2)+symbol1+symbol2

print(shuffle(password))
