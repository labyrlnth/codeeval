import sys
fib = [0, 1]
f = open(sys.argv[1], 'r')
numbers = f.readlines()
for number in numbers:
	n = int(number)
	while len(fib) - 1 < n:
		fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
	print fib[n]
		
	