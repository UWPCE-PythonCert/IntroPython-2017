
"""
Read sherlock_small.txt
Create the function of trigrams
"""

import random


def read_file():

    lines = []

    with open('sherlock_small.txt', 'r') as f:
        while True:
            line = f.readline().split()
            lines.extend(line)
            if not line:
                break
            # print(line)
    return lines

# words = read_file()


def trigrams(words):

    trigrams = {}

    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        # print(pair, follower)
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]  # key:pair

    return trigrams


def create_paragraph(trigrams_dict):

    # i = random.choice(list(tri_dict.keys()))
    paragraph_list = []
    paragraph_list.extend(random.choice(list(tri_dict.keys())))

    for d in range(20):
        pair = tuple(paragraph_list[-2:])
        # pair = tuple(pair)
        new_word = random.choice(tri_dict[pair])
        paragraph_list.append(new_word)
        # new_tuple = (i[1], new_word)
        # i = new_tuple
        # print(paragraph_list)
    print(" ".join(paragraph_list))


if __name__ == "__main__":
    words = read_file()
    # words = "I wish I may I wish I might.".split()
    tri_dict = trigrams(words)
    # print("tri_dict", tri_dict)
    create_paragraph(tri_dict)








