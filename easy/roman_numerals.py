import sys
dic = {3000 : 'MMM',
       2000 : 'MM',
       1000 : 'M',
       900  : 'CM',
       800  : 'DCCC',
       700  : 'DCC',
       600  : 'DC',
       500  : 'D',
       400  : 'CD',
       300  : 'CCC',
       200  : 'CC',
       100  : 'C',
       90   : 'XC',
       80   : 'LXXX',
       70   : 'LXX',
       60   : 'LX',
       50   : 'L',
       40   : 'XL',
       30   : 'XXX',
       20   : 'XX',
       10   : 'X',
       9    : 'IX',
       8    : 'VIII',
       7    : 'VII',
       6    : 'VI',
       5    : 'V',
       4    : 'IV',
       3    : 'III',
       2    : 'II',
       1    : 'I',}

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    for line in lines:
        if line:
            line = line.strip()
            number = int(line)
            result = []
            if number >= 1000:
                thousand = number - number % 1000
                result.append(dic[thousand])
                number = number - thousand
            if number >= 100:
                hundred = number - number % 100
                result.append(dic[hundred])
                number = number - hundred
            if number >= 10:
                ten = number - number % 10
                result.append(dic[ten])
                number = number - ten
            if number >= 1:
                result.append(dic[number])
            print ''.join(result)
