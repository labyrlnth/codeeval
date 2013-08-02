import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()

for line in lines:
	arg = line.split()
	for i in xrange(1, int(arg[2]) + 1):
		if i % int(arg[0]) == 0 and int(i) % int(arg[1]) != 0:
			print 'F',
		elif i % int(arg[0]) != 0 and int(i) % int(arg[1]) == 0:
			print 'B',
		elif i % int(arg[0]) == 0 and int(i) % int(arg[1]) == 0:
			print 'FB',
		else:
			print i,
	print
			