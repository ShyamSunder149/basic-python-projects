# Fibonacci sequence generator

print('Please enter the number of terms you want in Fibonacci sequence:')
n = int(input())

first = 0
second = 1

print('Fibonacci sequence:')
print(first)
print(second)

for i in range(n-2):
	temp = first+second
	print(temp)
	first = second
	second = temp



