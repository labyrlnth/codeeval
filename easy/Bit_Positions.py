import sys
f = open(sys.argv[1], 'r')
lines = f.readlines()
for line in lines:
	numbers = line.split(',')
	number = int(numbers[0])
	p1 = int(numbers[1])
	p2 = int(numbers[2])
	string = str(bin(number))
	if string[len(string) - p1] == string[len(string) - p2]:
		print 'true'
	else:
		print 'false'