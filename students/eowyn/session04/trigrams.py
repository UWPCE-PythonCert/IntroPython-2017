#!/usr/bin/env python

#words = "I wish I may I wish I might".split()
PUNCTUATION = ['.','!','?'] ## pg 125 of think python has line processing example

## TO DO write function to occasionally insert punctionation followed by capitalized letters
## Kinda did that but ought to take into account where trigrams begin/end
### TO DO: figure out how to properly capitalize I, proper nouns

import random
import string

def convert_text(filename):
    ''' 
    Convert the full text of a local filename (str) to 
    return the corresponding dictionary of trigrams
    '''
    words = []
    for lines in open(filename):
        words += process_line(lines)
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
    ''' Given a filename (str) and number, n, construct a 
    made-up text of n random trigrams from the text contained in filename.
    n should be an int and will otherwise be rounded to int.
    '''
    n = round(n)
    trigrams = convert_text(filename) # dictionary
    ntrigrams = len(trigrams)
    new_words = []
    for triplet in range(n):
        randokey = random.choice(list(trigrams)) # randomly select a LIST key from the dictionary
        randoval = random.choice(trigrams[randokey]) # randomly select a STRING value from the pre-selected key
        new_words += [randokey[0]] + [randokey[1]] + [randoval] # append triplet onto new word list
    process_output(new_words)
    new_words = " ".join(new_words)
    print(new_words)


def process_line(line):
    '''
    Remove punctionation, white space, and upper case from lines
    of text and return list of remaining words
    '''

    line.replace("-"," ")
    words = []
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        words += [word]
    return words

def process_output(word_list):
    i = 0
    #print("total number of words: ",len(word_list))
    while i < len(word_list):
        sentence_length = random.randint(6,12)
        #print("i: ",i," ,i plus sentence length: ",i+sentence_length)
        word_list[i] = word_list[i].capitalize()
        try:
            word_list[i+sentence_length-1] = word_list[i+sentence_length-1] + random.choice(PUNCTUATION)
        except:
            sentence_length = len(word_list) - i
            #print("new sentence length: ",sentence_length,"new last index: ",i+sentence_length)
            word_list[i+sentence_length-1] = word_list[i+sentence_length-1] + random.choice(PUNCTUATION)
        i += sentence_length




if __name__ == "__main__":
    construct_text("sherlock_small.txt",20)



