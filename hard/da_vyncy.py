import sys

def find_overlap(term1, term2, highest_overlap):
    overlap = -1
    overlap_reverse = -1
    length = min(len(term1), len(term2))
    for x in xrange(length, 0, -1):
        if x <= highest_overlap:
            break
        if term1[-x:]  == term2[:x]:
            overlap = x
            break
    for x in xrange(length, 0, -1):
        if x <= highest_overlap:
            break
        if term2[-x:]  == term1[:x]:
            overlap_reverse = x
            break
    if overlap >= overlap_reverse:
        return[overlap, False]
    else:
        return[overlap_reverse,True]
    
    

def merge(sentence):
    index_1 = -1
    index_2 = -1
    highest_overlap = -1
    order = True
    for outer_index in xrange(len(sentence)-1,0,-1):
        for inner_index in xrange(outer_index - 1, -1, -1):
            if min(len(sentence[outer_index]), len(sentence[inner_index])) <= highest_overlap:
                continue
            overlap, reverse = find_overlap(sentence[outer_index], sentence[inner_index], highest_overlap)
            if overlap > highest_overlap:
                highest_overlap = overlap
                index_1 = outer_index
                index_2 = inner_index
                order = reverse
    if index_1 == index_2 == -1:
        return sentence
    term1 = sentence[index_1]
    term2 = sentence[index_2]
    sentence.remove(term1)
    sentence.remove(term2)
    new_term = ''
    if not order:
        new_term = term1 + term2[highest_overlap:]
    else:
        new_term = term2 + term1[highest_overlap:]
    sentence.append(new_term)
    return sentence
                
        

if __name__ == '__main__':
    f = open(sys.argv[1],'r')
    lines = f.readlines()
    for line in lines:
        if line:
            line = line.strip()
            sentences = line.split(';')
            sentences.sort(key=len)
            count = len(sentences)
            while True:
                sentences = merge(sentences)
                if len(sentences) == count or len(sentences) == 1:
                    break
                else:
                    count -= 1
            result = ''
            for item in sentences:
                if len(item) > len(result):
                    result = item
            print result