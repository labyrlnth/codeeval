import sys, time

def get_all_values(number):
    if len(number) == 0:
        return []
    elif len(number) == 1:
        return [int(number)]
    else:
        result = []
        for x in xrange(1, len(number)+1):
            num = int(number[:x])
            expr = get_all_values(number[x:])
            if expr == []:
                result.append(num)
            else:
                for val in expr:
                    result.append(num + val)
                    result.append(num - val)
        return result
            

def get_ugly_count(values):
    count = 0
    for val in values:
        if val % 2 == 0 or val % 3 == 0 or val % 5 == 0 or val % 7 == 0:
            count += 1
    return count

if __name__ == '__main__':
    start = time.time()
    f = open(sys.argv[1],'r')
    lines = f.readlines()
    for line in lines:
        if line:
            line = line.strip()
            values = get_all_values(line)
            number = get_ugly_count(values)
            print number
