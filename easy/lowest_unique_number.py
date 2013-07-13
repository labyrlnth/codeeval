import sys

def main():
    f = open(sys.argv[1], 'r')
    lists = f.readlines()
    for line in lists:
        if line:
            line = line.strip()
            numbers = map(int, line.split())
            dic = {}
            for number in numbers:
                if number in dic:
                    dic[number] = dic[number] + 1
                else:
                    dic[number] = 1
            flag = True
            for key in sorted(dic.iterkeys()):
                if dic[key] == 1:
                    print numbers.index(key) + 1
                    flag = False
                    break
            if flag:
                print 0


if __name__ == "__main__":
    main()