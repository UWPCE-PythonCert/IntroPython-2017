#!/usr/bin/env python


import random
import string

# pg 125 of think python has line processing example
PUNCTUATION = ['.', '!', '?']

# TO DO: figure out how to properly capitalize I, proper nouns
# the I thing can be addressed with an if word == "i"
## look into using translate method to replace lots of things with other things
# TO DO: Fix trigrams that end in words like "and", prepositional phrases, articles


def convert_text(filename):
    ''' 
    Convert the full text of a local filename (str) to 
    return the corresponding dictionary of trigrams
    '''
    words = []
    for lines in open(filename):
        words += process_line(lines)
    trigrams = {}  # a dictionary
    for i in range(len(words) - 2):
        # doesn't include the last char, so this is a pair of words
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair,[]).append(follower)
    return trigrams


def construct_text(filename, n):
    ''' Given a filename (str) and number, n, construct a 
    made-up text of n random trigrams from the text contained in filename.
    n should be an int and will otherwise be rounded to int.
    '''
    n = round(n)
    trigrams = convert_text(filename)  # dictionary
    new_words = []
    for triplet in range(n):
        # randomly select a LIST key from the dictionary
        randokey = random.choice(list(trigrams))
        # randomly select a STRING value from the pre-selected key
        randoval = random.choice(trigrams[randokey])
        new_words += [randokey[0]] + [randokey[1]] + \
            [randoval]  # append triplet onto new word list
    process_output(new_words)
    new_words = " ".join(new_words)
    print(new_words)


def process_line(line):
    '''
    Remove punctionation, white space, and upper case from lines
    of text and return list of remaining words
    '''

    line.replace("-", " ")
    line.replace("--", " ")
    words = []
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        words += [word]
    return words


def process_output(word_list):
    '''
    Add random punctuation followed by capitalization to a list of words. Sentences are 
    between 4 and 18 words long hard-coded but must be multiples of 3 to have them 
    begin/end where trigrams begin/end.
    '''
    i = 0
    while i < len(word_list):
        sentence_length = random.randint(4, 18)
        while sentence_length % 3 != 0:
            sentence_length = random.randint(4, 18)
        word_list[i] = word_list[i].capitalize()
        try:
            word_list[i + sentence_length - 1] = word_list[i +
             sentence_length - 1] + random.choice(PUNCTUATION)
        except:
            sentence_length = len(word_list) - i
            word_list[i + sentence_length - 1] = word_list[i +
            sentence_length - 1] + random.choice(PUNCTUATION)
        i += sentence_length


if __name__ == "__main__":
    construct_text("sherlock.txt", 20)
