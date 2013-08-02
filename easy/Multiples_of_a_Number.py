import sys
f = open(sys.argv[1], 'r')
lines = f.readlines()
for line in lines:
	numbers = line.split(',')
	x = int(numbers[0])
	n = int(numbers[1])
	i = 1
	while x > n * i:
		i += 1
	print n * i