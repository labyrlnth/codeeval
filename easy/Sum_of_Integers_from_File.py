import sys

f = open(sys.argv[1], 'r')
numbers = f.readlines()
sum = 0
for number in numbers:
	sum += int(number)
print sum