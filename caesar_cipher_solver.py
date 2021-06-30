# caesar cipher solver

print('caesar cipher solver')
print('enter the ciphertext:')
s = input()
s.upper()

for i in range(1,26):
	print('--------------------------------------')
	print('key = {}'.format(i))
	c = ''
	for j in s:
		c+= chr((ord(j) + i-65) % 26 + 65)
	print(c)
