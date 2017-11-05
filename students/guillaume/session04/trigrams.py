#!/usr/bin/env python3
from os import system
from string import punctuation
from random import choice, randint
# import string
from collections import defaultdict
'''
words = 'I wish I may I wish I might'.split()

print(words)

trigrams = {}
for i in range(len(words) - 2):
    pair = tuple(words[i:i + 2])
    follower = words[i + 2]
    if pair in trigrams:
        trigrams[pair].append(follower)
    else:
        trigrams[pair] = [follower]
'''


# print(trigrams)

def add_line_to_dict(dic, words):
    ''' '''
    for i in range(len(words) - 2):
        pair = tuple(words[i: i + 2])
        follower = words[i + 2]
        dic[pair].append(follower)
    return dic


def remove_punctuation(line):
    '''
    remove the punctuation of the text using a translation table
    by translating any punctuation character into a space
    '''
    table = str.maketrans(punctuation, ' ' * len(punctuation))
    line_out = line.translate(table)
    return line_out


def trigrams(textfile_in, textfile_out):
    '''reading method is acceptable for big textfile'''
    start = None
    start_novel = 'Produced by an anonymous Project Gutenberg'
    l_s = len(start_novel)
    end_novel = 'End of the Project Gutenberg EBook'
    l_e = len(end_novel)
    dic = defaultdict(list)
    with open(textfile_in) as fileread:
        for line in fileread:
            if line[:l_s] == start_novel:
                start = True
            elif line[:l_e] == end_novel:
                break
            elif line is not '\n' and start:
                line = remove_punctuation(line)
                words = line.split()
                dic = add_line_to_dict(dic, words)
    fileread.close
    dic = dict(dic)

    with open(textfile_out, 'w') as filewritten:
        for _ in range(1000):
            rand_paragraph = randint(1, 25)
            if rand_paragraph == 25:
                new_line = '\n'
            else:
                new_line = str()
            rand_range = randint(2, 4)
            for _ in range(rand_range):
                rand_key = choice(list(dic))
                rand_item_lst = choice(dic[rand_key])
                rand_punc = choice(list('!"\',.:;?'))
                new_line += '{} {} '.format(' '.join(rand_key), rand_item_lst)
                rand_val = randint(1, 6)
                if rand_val == 6:
                    new_line = '{}{} '.format(new_line[: -1], rand_punc)
            new_line += '\n'
            filewritten.write(new_line)
    filewritten.close()


if __name__ == '__main__':
    trigrams('sherlock.txt', 'sherlock_trigrams.txt')
    system('subl sherlock_trigrams.txt')
