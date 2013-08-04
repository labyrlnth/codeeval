import sys

def generate_strings(letters, number):
    if number == 0:
        return []
    else:
        result = []
        rest = generate_strings(letters, number - 1)
        for letter in letters:
            if rest == []:
                return letters
            else:
                for item in rest:
                    new_string = ''.join([letter, item])
                    result.append(new_string)
        return result


if __name__ == '__main__':
    f = open(sys.argv[1],'r')
    lines = f.readlines()
    for line in lines:
        if line:
            line = line.strip()
            number, letters = line.split(',')
            number = int(number)
            letters = list(set(letters))
            letters.sort()
            result = generate_strings(letters, number)
            print ','.join(result)
            
                
           

