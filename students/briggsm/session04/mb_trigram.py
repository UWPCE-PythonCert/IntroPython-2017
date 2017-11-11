import random as rand

def create_corpus(infile):
    '''Input: a filename
       Output: a list of words.'''
    corpus = []
    with open(infile) as lines:
        lines.readline()
        for line in lines:
            line = line.strip()
            words = line.split(" ")
            for i in range(len(words)):
                corpus.append(words[i])
    return corpus

def create_trigram(textlist):
    '''Input: a list of words from a text body.
       Output: a dictionary of two words in sequence and the word after.'''
    trigram = {}
    for w in range(len(textlist[:-2])):
        firstword = textlist[w]
        secondword = textlist[w+1]
        thirdword = textlist[w+2]
        trigram[thirdword] = (firstword, secondword)
    return trigram

def get_values(trigram):
    '''Input: a dictionary.
       Output: a list of keys.'''
    words = []
    for w in trigram.keys():
        words.append(w)
    return words

def get_random_item(listofwords):
    '''Input: a list of items.
       Output: a random item as a string.'''
    choose = rand.randint(0,len(listofwords))
    return str(listofwords[choose])

def create_random_text(listofwords, trigram, wordcount):
    outstring = ""
    for i in range(wordcount):
        pick = get_random_item(listofwords)
        getpair = trigram[pick]
        outstring += getpair[0] + " " + getpair[1] + " "
    return outstring

if __name__ == "__main__":
    text_body = create_corpus("text.txt")
    threegram = create_trigram(text_body)
    listofwords = get_values(threegram)
    mystory = create_random_text(listofwords, threegram, 250)
    print (mystory)