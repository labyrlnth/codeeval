import sys
f = open(sys.argv[1], 'r')
lines = f.readlines()
for line in lines:
	print line.lower()