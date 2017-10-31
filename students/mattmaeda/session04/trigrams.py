#!/usr/bin/env python3
import re
from random import randint

def convert_to_word_list(book_text):
    raw_list =  re.sub('[^0-9a-zA-Z]+', ' ', book_text).split(" ")
    return [word.lower() for word in raw_list if word != ""]


def build_word_dict(word_list):
    word_dict = {}
    for i in range(len(word_list)-2):
        pair = tuple(word_list[i:i+2])
        follower = word_list[i+2]
        word_dict.setdefault(pair, []).append(follower)

    return word_dict


def build_new_text(word_dict):
    rand_idx = randint(0, len(word_dict.keys()))
    new_list = []

    idx = 0

    start_follower_arr = None

    for k,v in word_dict.items():
        if rand_idx == idx:
            new_list.append(k[0])
            new_list.append(k[1])
            new_list = append_next_word(new_list, v)
            break
        idx += 1

    last_two = tuple(new_list[-2:])

    while True:
        try:
            new_list = append_next_word(new_list, word_dict[last_two])
            last_two = tuple(new_list[-2:])
        except KeyError:
            break

    return new_list


def append_next_word(new_word_list, possible_words):
    if len(possible_words) == 1:
        new_word_list.append(possible_words[0])
    else:
        rand_idx = randint(0, (len(possible_words)-1))
        new_word_list.append(possible_words[rand_idx])

    return new_word_list

if __name__ == "__main__":
    book_file = "sherlock_small.txt"
    fh = open(book_file)
    text = convert_to_word_list(fh.read())
    word_dict = build_word_dict(text)
    new_text = build_new_text(word_dict)
    print(" ".join(new_text))
