import sys

dic = {'one':'1',
       'two':'2',
       'three':'3',
       'four':'4',
       'five':'5',
       'six':'6',
       'seven':'7',
       'eight':'8',
       'nine':'9',
       'zero':'0'}
       
def word_to_digit(word):
    return dic[word]
       
def main():
    f = open(sys.argv[1], 'r')
    lists = f.readlines()
    for line in lists:  
        if line:
            line = line.strip()
            words = line.split(';')
            print "".join(map(word_to_digit, words))
            
if __name__ == "__main__":
    main()