#!/usr/bin/env python

words = 'I wish I may I wish I might'.split()

print(words)

trigrams = {}
for i in range(len(words)-2):
	pair = tuple(words[i:i+2])
	follower = words[i+2]
	print('Pair and follower: ', pair, follower)
	if pair in trigrams:
		trigrams[pair].append(follower)
	else:
		trigrams[pair] = [follower]

print('Trigrams: ', trigrams)

#print(trigrams[pair][follower])
#print('Printing the dict value: ', trigrams[('I', 'wish')])



#for key, value in trigrams.items():
#    print ('Key and value: ', key, value)

new_var = trigrams[('wish', 'I')][0]
new_var2 = trigrams[('wish', 'I')][1]
print('new_var: ', new_var)
print('new_var2: ', new_var2)

newlist = list()
newerlist = list()
j = 0
for i in trigrams.keys():
    newlist.append(i)
    var1, var2 = newlist[j]
    print('Keys extracted: ', var1, var2, *trigrams[i])
    j += 1

import random

which_list, item = random.choice([(name, value) for name, values in trigrams.items() for value in values])
pair_word1, pair_word2 = which_list
print('which_list: ', which_list)
print('item: ', item)
print('String: ', pair_word1, pair_word2, item)

#for i in range(5):
#	for j in range(5):
#		print(i, ':', trigrams[i][j])