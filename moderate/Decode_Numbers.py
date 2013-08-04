import sys

if __name__ == '__main__':
    f = open(sys.argv[1],'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        result = [1,1]
        for index in xrange(1, len(line)):
            if int(line[index-1:index+1])<=26:
                result.append(result[-1]+result[-2])
            else:
                result.append(result[-1])
        print result[-1]

