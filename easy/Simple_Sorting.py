import sys

if __name__ == '__main__':
    f = open(sys.argv[1],'r')
    lines = f.readlines()
    for line in lines:
        if line:
            line = line.strip()
            float_list = map(float,line.split())
            float_list.sort()
            print ' '.join(map(lambda x: "{0:.3f}".format(x) ,float_list))

