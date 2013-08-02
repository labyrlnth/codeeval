prime = []
for i in xrange(2, 1000):
	for j in xrange(2, i):
		if i % j == 0:
			break 
	else:
		prime.append(i)
i = len(prime) - 1
while True:
	number = str(prime[i])
	if number[0] == number[2]:
		print number
		break
	else:
		i -= 1
		continue
		