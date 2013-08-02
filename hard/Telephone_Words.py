import sys
dic = { '0':'0',
        '1':'1',
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz', }

def translate(line_list):
    if not line_list:
        return []
    else:
        result = []
        first_list = list(dic[line_list[0]])
        rest = translate(line_list[1:])
        if not rest:
            return first_list
        else:
            for item_first in first_list:
                for item_rest in rest:
                    result.append(''.join([item_first, item_rest]))
            return result

if __name__ == '__main__':
    f = open(sys.argv[1],'r')
    lines = f.readlines()
    for line in lines:
        if line:
            line = line.strip()
            line_list = list(line)
            result = translate(line_list)
            result.sort()
            print ','.join(result)
