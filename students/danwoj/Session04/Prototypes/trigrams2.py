#!/usr/bin/env python
#words = 'I wish I may I wish I might'.split()

infile = 'sherlock_small.txt'

all_words = []
with open(infile) as novel:
	novel.readline()
	for line in novel:
		line = line.strip()
		split_line = line.split()
		all_words.extend(split_line)
#		print('This is split_line: ', split_line)
#		print('This is line: ', line)

new_words = []
for i in all_words:
	if i.strip():
		new_words.append(i.strip())

#new_langs = [lang.strip() for lang in all_langs if lang.strip()]

all_words = set(new_words)

#print('This is new_words: ', new_words)

#print('This is words: ', words)

trigrams = {}
for i in range(len(new_words)-2):
	pair = tuple(new_words[i:i+2])
	follower = new_words[i+2]
#	print('Pair and follower: ', pair, follower)
	if pair in trigrams:
		trigrams[pair].append(follower)
	else:
		trigrams[pair] = [follower]

counter = (len(trigrams.keys()))//3

print('Counter: ', counter)

#print('This is trigrams: ', trigrams)

import random

for i in range(counter):
	which_list, item = random.choice([(name, value) for name, values in trigrams.items() for value in values])
	pair_word1, pair_word2 = which_list
	#print('which_list: ', which_list)
	#print('item: ', item)
	print(pair_word1, pair_word2, item, '', end='')
print('.')