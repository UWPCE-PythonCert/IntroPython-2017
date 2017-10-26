#!/usr/bin/env python3

"""

trigrams

"""
import random

words = """
One night--it was on the twentieth of March, 1888--I was
returning from a journey to a patient (for I had now returned to
civil practice), when my way led me through Baker Street. As I
passed the well-remembered door, which must always be associated
in my mind with my wooing, and with the dark incidents of the
Study in Scarlet, I was seized with a keen desire to see Holmes
again, and to know how he was employing his extraordinary powers.
His rooms were brilliantly lit, and, even as I looked up, I saw
his tall, spare figure pass twice in a dark silhouette against
the blind. He was pacing the room swiftly, eagerly, with his head
sunk upon his chest and his hands clasped behind him. To me, who
knew his every mood and habit, his attitude and manner told their
own story. He was at work again. He had risen out of his
drug-created dreams and was hot upon the scent of some new
problem. I rang the bell and was shown up to the chamber which
had formerly been in part my own.
""".split()

# words = "I wish I may I wish I might".split()


# function to make pairs and followers
def make_trigrams(words):
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follower = words[i+2]
        print(pair, follower)
        if pair in trigrams:
            trigrams[pair].append(follower)
        trigrams[pair] = [follower]

# function to randomly select pairs and followers
def select_trigrams():
    pass
# function to write a new file

#main function, open & read file, split file, make_trigrams,
if __name__ == "__main__":
    f = "sherlock_small.txt"
    t = open(f)
    text =(t.read())
    text = text.split()
    make_trigrams(text)
