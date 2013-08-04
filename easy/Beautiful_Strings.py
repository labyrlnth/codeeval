import sys
f = open(sys.argv[1], 'r')
list = f.readlines()
for line in list:
    line = line.strip()
    line = line.lower()
    items = set(line)
    beauties = []
    value = 0
    for i in items:
        if not i.isalpha():
            continue
        beauties.append(line.count(i))
    beauties.sort(reverse = 1)
    current = 26
    for i in beauties:
		value += i * current
		current -= 1
    print value
