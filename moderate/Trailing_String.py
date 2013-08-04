import sys
f = open(sys.argv[1], 'r')
lines = f.readlines()
for line in lines:
	line = line.strip()
	long, short = line.split(',')
	if long.endswith(short):
		print '1'
	else:
		print '0'