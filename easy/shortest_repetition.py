import sys
f = open(sys.argv[1],'r')
lines = f.readlines()
for line in lines:
    if line:
        line = line.strip()
        for index in xrange(1,len(line)+1):
            if len(line) % index == 0:
                elem = line[0:index]
                for pos in xrange(0,len(line),index):
                    if elem != line[pos:pos+index]:
                        break
                else:
                    print index
                    break

