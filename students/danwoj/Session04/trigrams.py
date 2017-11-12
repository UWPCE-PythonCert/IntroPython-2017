#!/usr/bin/env python

infile = 'sherlock_small.txt'
#infile = 'sherlock.txt'

# This reads all the words in the input file and puts it in a list.
all_words = []
with open(infile) as novel:
	novel.readline()
	for line in novel:
		line = line.strip()
		split_line = line.split()
		all_words.extend(split_line)

new_words = []
for i in all_words:
	if i.strip():
		new_words.append(i.strip())

#new_langs = [lang.strip() for lang in all_langs if lang.strip()]

all_words = set(new_words)

trigrams = {}
for i in range(len(new_words)-2):
	pair = tuple(new_words[i:i+2])
	follower = new_words[i+2]
	if pair in trigrams:
		trigrams[pair].append(follower)
	else:
		trigrams[pair] = [follower]

'''
Ths variable 'counter' sets the length of the trigrams test an output 
which is approximately the same size as the original text file that was read.
'''

counter = (len(trigrams.keys()))//3

'''
To be completely honest, I found the random function in the following 
 for loop on the Internet. It sounded like the person asking for this 
 had the exact same situation as I did and it happens to work. I'm still 
 trying to understand everything it's doing.
'''

import random

f = open("trigrams-output.txt","w") # Opens file for text output.
for i in range(counter):
	which_list, item = random.choice([(name, value) for name, values in trigrams.items() for value in values])
	pair_word1, pair_word2 = which_list

'''
The following conditionals check for the the first and last input. 
 If it's the first, it ensures the sentence begins with a capital letter. 
 If it's the last, it adds a period to end the late sentence.
'''

	if i == 0:
		text_output = pair_word1.capitalize() + ' ' + pair_word2 + ' ' + item + ' '
		s = str(text_output)
		f.write(s)		
	elif i < counter-1:
		text_output = pair_word1 + ' ' + pair_word2 + ' ' + item + ' '
		s = str(text_output)
		f.write(s)
	else:
		text_output = pair_word1 + ' ' + pair_word2 + ' ' + item + '.'
		s = str(text_output)
		f.write(s)	
f.close()