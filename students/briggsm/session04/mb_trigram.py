''''
Matt Briggs Trigram Exercise
Version 2.0 2017.11.19
'''

import random as rand


def create_corpus(infile):
    ''' Input: a filename of a text file
        Output: a list of words from the text file.'''
    corpus = []
    with open(infile) as lines:
        lines.readline()
        for line in lines:
            line = line.strip()
            words = line.split(" ")
            for word in enumerate(words):
                corpus.append(word[1])
    return corpus


def create_trigram(textlist):
    ''' Input: a list of words from a text body.
        Output: a dictionary of two words in sequence and the word after.'''
    trigram = {}
    for x in range(len(textlist[:-2])):
        firstword = textlist[x]
        secondword = textlist[x+1]
        thirdword = textlist[x+2]
        #print("[({},{}] = {}".format(firstword, secondword, thirdword))
        if (firstword, secondword) in trigram:
            trigram[(firstword, secondword)].append(thirdword)
        else:
            trigram[(firstword, secondword)] = [thirdword]
    return trigram


def get_values(trigram):
    '''Input: a dictionary.
       Output: a list of word pair keys.'''
    words = []
    for w in trigram.keys():
        words.append(w)
    return words


def create_new_corpus(trigram, listofwordpairs, wordcount):
    ''' Input: trigram dictionary, trigrams list of word pairs as a list, wordcount resulttext
        Output: a list of the containing the new text.'''
    seed = rand.choice(listofwordpairs)
    new_corpus = []
    new_corpus.append(seed[0])
    new_corpus.append(seed[1])
    for i in range(1, wordcount):
        if (new_corpus[i-1], new_corpus[i]) in listofwordpairs:
            new_corpus.append(rand.choice(trigram[(new_corpus[i-1], new_corpus[i])]))
        else:
            seedit = rand.choice(listofwordpairs)
            new_corpus.append(rand.choice(trigram[seedit]))
    return (new_corpus)


def create_text_from_list(word_list):
    ''' Input: A list containing the words in order.
        Output: a single string.'''
    output = ""
    for word in word_list:
        output += word + " "
    return output


if __name__ == "__main__":
    infile = input("Type the filename of a text to use for the trigram. > ")
    wordcount = int(input("Type the number of words in the generated text. > "))
    text_body = create_corpus(infile)
    threegram = create_trigram(text_body)
    listofwordpairs = list(threegram)
    new_text_list = create_new_corpus(threegram, listofwordpairs, wordcount)
    story = create_text_from_list(new_text_list)
    print(story)
