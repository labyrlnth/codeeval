import sys
f = open(sys.argv[1], 'r')
lines = f.readlines()
for line in lines:
	words = line.split()
	if len(words) != 0:
		for i in xrange(len(words) - 1, -1, -1):
			print words[i],
		print
		
		