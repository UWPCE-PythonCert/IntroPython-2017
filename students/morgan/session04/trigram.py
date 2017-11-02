#1/usr/bin/env python

import re
import random
# words = 'I wish I may I wish I might'.split()

words = []
infile = 'sherlock.txt'
# ignore first 61 lines
with open(infile) as book:
    # book.readline() * 61
    for line in book:
        line = re.split('\s|--' ,line.strip())
        words += line



print(words)

'''this builds the complete library from source text'''
trigram = {}
for i in range(len(words)-2):
    pair = words[i:i+2]
    follower = words[i+2]
    print(pair, follower)
    trigram.setdefault(tuple(pair),[]).append(follower)
    # trigram[tuple(pair)].append(follower)


    # if pair in trigram:
    #   trigram[pair].append(follower)
    # else:
    #   trigram[pair] = [follower]

print(trigram)


count = int(input('how many items to create?'))

phrase = []

phrase += list(random.choice(list(trigram)))
print(phrase)
# random.choice(trigram[tuple(phrase[-2:])])

# derp = len(trigram['I', 'wish'])
# print(trigram['I', 'wish'])
# print(derp)

a = tuple(phrase[-2:])

# i=0
while len(phrase) < count :
    if tuple(phrase[-2:]) in trigram:
        print(trigram[tuple(phrase[-2:])], 'values')
        phrase.append(random.choice(trigram[tuple(phrase[-2:])]))
        print(phrase, 'phrase')
        
    else:
        print('oops')
        break
    # i += 1

print(' '.join(phrase))
input('')



# '''
# a b c d
# {a:b} c
# {b:c} d

# randomly grab out two followers, compare to see if there is a key match
# 1)
# if match is true, print key and follower
# if match is false, grab two new seeds and check again.
# 2)
# for the new list being populated, check the last two values [-2:] and 
# compare if there is a matching key.
# If key = true, print follower
# if key = false, print random follower to random key
#   '''