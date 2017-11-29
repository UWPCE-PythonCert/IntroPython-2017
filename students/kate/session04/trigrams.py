#!/usr/bin/env python3

"""
trigrams with sherlock writing
"""
# import random module
from random import randint

# function to make pairs and followers in trigram dictionary
def gen_trigrams(words):
    # make an empty dicitonary for the trigrams
    trigrams_dict = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follower = words[i+2]
        # print(pair, follower)
        if pair in trigrams_dict:
            trigrams_dict[pair].append(follower)
        trigrams_dict[pair] = [follower]
    else:
        trigrams_dict[pair].append(follower)
    return(trigrams_dict)

def build_new_text(word_dict):
    # create index to hold a random integer
    rand_index = randint(0, len(word_dict))
    # create list to hold words
    new_list = []
    # set counter to 0
    index = 0

    # build sentences using index counter. Use for loop to add keys and values

    for keys,values in word_dict.items():
        if rand_index == index:
            new_list.append(keys[0])
            new_list.append(keys[1])
            new_list = append_next_word(new_list, values)
            # print(new_list)
            break
        index += 1
    last_two = tuple(new_list[-2:])

    while True:
        try:
            new_list = append_next_word(new_list, word_dict[last_two])
            last_two = tuple(new_list[-2:])
        except KeyError:
            break

    return new_list

def append_next_word(new_word_list, words):
    if len(words) == 1:
        new_word_list.append(words[0])
    else:
        rand_index = randint(0, (len(words)-1))
        new_word_list.append(words[rand_index])
    return new_word_list

# main function
# use functions: make trigrams
if __name__ == "__main__":
    # open & read file, split file,
    f = "sherlock_small.txt"
    t = open(f)
    w =(t.read())
    w = w.split()

    # run supporting functions
    trigram_list = gen_trigrams(w)
    new_text = build_new_text(trigram_list)

    # display new text on screen, write new file to save text
    print(" ".join(new_text))
    x = open("new_book.txt", "w+")
    x.write(" ".join(new_text))
