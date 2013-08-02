import math
prime = []
i = 2
while len(prime) < 1000:
	for j in xrange(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			i += 1
			break 
	else:
		prime.append(i)
		i += 1
	continue

sum = 0
for number in prime:
	sum += number
print sum
		
		