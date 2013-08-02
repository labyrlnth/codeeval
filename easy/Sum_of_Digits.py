import sys
f = open(sys.argv[1], 'r')
numbers = f.readlines()
for number in numbers:
	sum = 0
	for i in xrange(len(number)):
		try:
			sum += int(number[i])
		except:
			pass
	print sum
	