#!/usr/bin/env python
import random

infile = 'sherlock_small.txt'

def removePunc():
    """ removing punctuations and white space from lines of text and return list of remaining words"""
    line_list = []
    with open(infile, 'r') as fin:
        for line in fin:
            line = line.strip().replace('-', ' ')
            line = "".join(p for p in line if p not in ('.', ',', '(', ')'))
            line_list.append(line)

    return line_list

def build_trigram(words):
    """ build a trigram dict """
    pairs = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        print(pair, follower)
        pairs.setdefault(pair, []).append(follower)

    return pairs

#TODO: need to go back and clean up text

if __name__ == "__main__":
    build_trigram(removePunc())