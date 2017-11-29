#!/usr/bin/env python

import string
import random

# Create an empty dictionary
trig = {}
# An empty list for word pool
wpool = []

def build_pool(inf):
    """ Build a pool of words from the input text file """
    with open(inf, 'r') as lines:
        # strip the line, make it all lower cases, remove punctuations, then make a new list
        for line in lines:
            wpool.extend(line.strip().lower().translate(str.maketrans('', '', string.punctuation)).split())

        # change individual 'i' with 'I'
        for wordi in range(len(wpool)):
            if wpool[wordi] == 'i':
                wpool[wordi] = 'I'

def build_trigram():
    """ Build a trigram library with a dictionary """
    for wordi in range(len(wpool)-2):
        pair = (wpool[wordi], wpool[wordi+1])
        if pair in trig:
            trig[pair].append(wpool[wordi+2])
        else:
            trig[pair] = [wpool[wordi+2]]

def random_output():

    # Random choice between comma and period
    somepun = [',', '.']
    # An empty string and list for new article
    news = ''
    # A flag to device id the phrase needs to be capitalized
    capflag = True

    # Outer loop to generate random phrases
    for i in range(random.randint(15, 25)):
        newt = random.choice(list(trig))
        newl = list(newt)
        # Inner loop to generate random words
        for j in range(random.randint(5, 10)):
            if newt in trig:
                newl.append(random.choice(trig[newt]))
                newt = tuple(newl[-2:])
        if capflag is True:
            newl[0] = newl[0].capitalize()
        pun = random.choice(somepun)
        newl[-1] += pun
        # Set flag for capitalization
        if pun == ',':
            capflag = False
        else:
            capflag = True
        news = news + ' ' + ' '.join(newl)
    # Make sure the article ends with a period
    news = news[:-1] + '.'
    return news




if __name__ == '__main__':
    """ Main function """
    build_pool('sherlock.txt')
    build_trigram()
    print(random_output())