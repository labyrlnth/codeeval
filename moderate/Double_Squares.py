import sys, math
f = open(sys.argv[1], 'r')
lines = f.readlines()
for line in lines[1:]:
    line.strip()
    n = int(line)
    count = 0
    i = 0
    j = int(1 + math.sqrt(n))
    while i <= j:
        s = i * i + j * j
        if s < n:
            i +=  1
        elif s > n:
            j -= 1
        else:
            count += 1
            i += 1
            j -= 1
    print count