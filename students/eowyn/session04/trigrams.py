#!/usr/bin/env python

#words = "I wish I may I wish I might".split()
PUNCTUATION = ['.','!','?'] ## pg 125 of think python has line processing example

## TO DO: add line processing. Also write function to occasionally insert punctionation followed by capitalized letters

import random


def convert_text(filename):
    ''' 
    Convert the full text of a local filename (str) to 
    return the corresponding dictionary of trigrams
    '''
    words = []
    for lines in open(filename):
        words += lines.split()
        ## TO DO: Add additional line processing
    trigrams = {} # a dictionary
    for i in range(len(words)-2):
        pair = tuple(words[i:i+2]) # doesn't include the last char, so this is a pair of words
        follower = words[i+2]
        if pair in trigrams:  
        ## TO DO: should be able to do this in one call... find that dictionary method
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower] # assign a key - value , key must be immutable
    return trigrams

def construct_text(filename,n):
    ''' Given a filename (str) and number of words, n, construct a 
    made-up text of random trigrams from the text contained in filename.
    n should be an int and will otherwise be rounded to int.
    '''
    n = round(n)
    trigrams = convert_text(filename) # dictionary
    ntrigrams = len(trigrams)
    new_words = []
    for triplet in range(n):
        randokey = random.choice(list(trigrams)) # randomly select a STRING key from the dictionary
        randoval = random.choice(trigrams[randokey]) # randomly select a LIST value from the pre-selected key
        new_words += [randokey] + [randoval] # append triplet onto new word list
    print(new_words)






if __name__ == "__main__":
    construct_text("sherlock_small.txt",20)



