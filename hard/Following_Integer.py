import sys

def get_next(number):
    #split the number into list
    new_number_list = map(int, list(number))
    #scan the list from right to left, and find the first digit that is smaller than the one right to it. if we reach the leftmost of the list, we have to add more digits beacuse the current is the biggest
    for x in xrange(len(new_number_list)-1, -1, -1):
        #if we reach the end of the list, we should reverse the current list, shifting the leading 0's with the first non-zero digit next to them, then add one more 0 after these 0s.
        if x == 0:
            new_number_list.reverse()
            for index in xrange(len(new_number_list)):
                if new_number_list[index] != 0:
                    temp = new_number_list[index]
                    new_number_list[index] = 0
                    new_number_list.insert(0,temp)
                    return ''.join(map(str,new_number_list))
        #otherwise we could switch this digit with the first digit in the tail that is bigger than it, then reverse the tail
        else:
            if new_number_list[x] > new_number_list[x-1]:
                #we find this digit at index x-1, we need to find the one that is bigger than it now
                for index in xrange(len(new_number_list)-1,x-1,-1):
                    if new_number_list[index]>new_number_list[x-1]:
                        temp = new_number_list[x-1]
                        new_number_list[x-1] = new_number_list[index]
                        new_number_list[index] = temp
                        temp_list = new_number_list[x:]
                        temp_list.reverse()
                        new_list = new_number_list[:x] + temp_list
                        return ''.join(map(str,new_list))

    

if __name__ == '__main__':
    f = open(sys.argv[1],'r')
    lines = f.readlines()
    for line in lines:
        if line:
            number = line.strip()
            new_number = get_next(number)
            print new_number
