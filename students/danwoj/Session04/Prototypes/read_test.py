#!/usr/bin/env python

'''
Parse students.txt file to get languages used by students
'''

#infile = 'students.txt'
infile = 'sherlock_small.txt'

all_langs = []
trigrams = {}
with open(infile) as novel:
	novel.readline()
	for line in novel:
		i = 0
		print('This is line: ', line)
		line = line.strip()
#		langs = line.split(':')[1].split(',')
		langs = line.split()
		pair = tuple(langs[i:i+2])
#		follower = langs[i+2]
		print('This is langs: ', langs)
		print('This is pair: ', pair)
#		print('This is follower', follower)
		i += 1
#		if langs[0].strip()[0].isupper():
#			langs = langs[1:]
		all_langs.extend(langs)

		print(langs)

#new_langs = []
#for lang in all_langs:
#	if lang.strip():
#		new_langs.append(lang.strip())

new_langs = [lang.strip() for lang in all_langs if lang.strip()]

all_langs = set(new_langs)


#trigrams = {}
#for i in range(len(words)-2):
#	pair = tuple(words[i:i+2])
#	follower = words[i+2]
#	print(pair, follower)
#	if pair in trigrams:
#		trigrams[pair].append(follower)
#	else:
#		trigrams[pair] = [follower]
#
#print(trigrams)