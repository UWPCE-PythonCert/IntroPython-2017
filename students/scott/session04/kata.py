#!/usr/bin/env python

import re
import random

text_file = "sherlock_small.txt"  # Define the name of the text file

text_file_open = open(text_file)

# raw_words is the entire raw contents of the text file
raw_words = text_file_open.read()

words_list = ""  # need to define _words_list


def make_words(text):
    words_list = re.sub('[^0-9a-zA-Z]+', ' ', raw_words).split(" ")
    print(len(words_list))
    del words_list[len(words_list)-1]
    trigrams = {}  # make empty dict
    for i in range(len(words_list)-2):
        pair = tuple(words_list[i:i+2])
        follower = words_list[i+2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams


trigrams = make_words(words_list)
# so now we've got our full list of trigrams and pairs

# Now to build the new story!


def write_new_story(input_dict):
    new_story = []
    start_pair = random.choice(list(trigrams.keys()))

    for i in range(len(trigrams)):
        if start_pair in trigrams.keys():
            new_word = random.choice(trigrams[start_pair])
            '''dicts are not indexed, however you use similar syntax
            to indexing, but you pass in a key value, not an index number'''
            new_start_pair = (start_pair[1], new_word)
            '''i needed parentheses to make this a tuple,
            since dictionary keys are tuples and you need to
            have a tuple to find that key in the dictionary'''
            start_pair = new_start_pair
            new_story.append(new_word)
    return ' '.join(new_story)


final_story = write_new_story(trigrams)
print(final_story)
print(len(final_story))