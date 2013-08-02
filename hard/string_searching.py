import sys

def replace_escape(item):
    nlist = list(item)
    for index, value in enumerate(nlist):
        if value == '*' and nlist[index-1] == '\\':
            nlist[index - 1] = ''
    return ''.join(nlist)

def find_first_appearance(item, first):
    for x in xrange(0, len(first) - len(item) + 1):
        if item == first[x:x + len(item)]:
            return x
    return -1

def is_substring(first, second):
    #split the second string by '*'
    nlist = []
    prev_index = 0
    second_list = list(second)
    for index, value in enumerate(second_list):
        if value == '*' and second_list[index - 1] != '\\':
            nlist.append(''.join(second_list[prev_index:index]))
            prev_index = index + 1
            continue
        if index == len(second_list) - 1:
            nlist.append(''.join(second_list[prev_index:]))
    #replace '\*' by 'x'
    for index, item in enumerate(nlist):
        if '\*' in item:
            nlist[index] = replace_escape(item)
    for item in nlist:
        if len(item) > len(first):
            return 'false'
        else:
            f_index = find_first_appearance(item, first)
            if f_index == -1:
                return 'false'
            else:
                first = first[f_index + len(item):]
    return 'true'

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    for line in lines:
        if line:
            first, second = map(lambda x: x.strip(), line.split(','))
            result = is_substring(first, second)
            print result
