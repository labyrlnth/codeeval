import sys, re
f = open(sys.argv[1], 'r')
lines = f.readlines()
for line in lines:
	if line:
		line = line.strip()
		nlist = re.findall(r'Label \d+', line)
		count = 0
		for label in nlist:
			n = int(label.split()[1])
			count += n
		print count