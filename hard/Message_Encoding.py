import sys

def split_data_set(line):
    for x in xrange(len(line)-1):
        if line[x].isdigit():
            return [line[:x], line[x:]]

def inc_key(key):
    key_list = list(key)
    for x in key_list[:-1]:
        if x != '1':
            break
    else:
        return '0' * (len(key_list) + 1)
    for x in xrange(len(key_list)-1,-1,-1):
        if key_list[x] == '0':
            key_list[x] = '1'
            break
        else:
            key_list[x] = '0'
    return ''.join(key_list)

def cons_dic(header):
    dic = {}
    key_start = '0'
    key = ''
    for x in xrange(len(header)):
        if x == 0:
            key = key_start
        else:
            key = inc_key(key)
        dic[key] = header[x]
    return dic

def all_1(msg):
    for x in list(msg):
        if x != '1':
            return False
    return True

def decode(dic, message):
    length_dic = {  '001':1,
                    '010':2,
                    '011':3,
                    '100':4,
                    '101':5,
                    '110':6,
                    '111':7,}
    result = []
    while True:
        length = message[:3]
        message = message[3:]
        if length == '000':
            #end of the message
            break
        else:
            length_num = length_dic[length]
            #start reading message
            while True:
                next_key = message[:length_num]
                message = message[length_num:]
                if all_1(next_key):
                    break
                else:
                    result.append(dic[next_key])
    return ''.join(result)



if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    for line in lines:
        if line:
            line = line.strip()
            header, message = split_data_set(line)
            #construct dictionary
            dic = cons_dic(header)
            #decode message
            result = decode(dic, message)
            print result
