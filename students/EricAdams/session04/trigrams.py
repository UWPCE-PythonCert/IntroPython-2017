#! /usr/bin/env python
# This scripts takes as input a text file named sherlock.txt
# The output is trigrams.txt text file.
#
# The set of data will be in the form of a trigram created as follows:
#         Look at each set of three adjacent words in a document.
#         Use the first two words of the set as a key, and remember
#         the fact that the third word followed that key.
#         So the trigram will look like:
#         {(word1, word2): [word3, next_word, ...],
#         (word2, word3): [list of words that follow word2 and word3], ...}.
#         To get the next_word value, search the text for all words that follow
#         word1 and word2 pair.

# To generate the output text file from the trigram,
#         choose an arbitrary word pair from the dict as a starting point.
# Use this pair to look up a random next word (using the trigram above) and
#           append this new word to the output file.
# This now gives a new word pair at the end of the output file.
# Look up a potential next word, using the trigram, based on these.
# Add this to the output file, and so on.
# Eventually the potential next word won't be in the trigram.
# At this point this script will write the final output
# The final output file will be a mutated form of the input text file.

# List of chars to remove or replace with a space from input text

import random

raw_input_list = []
input_list = []
initial_trigram_key = tuple()
output_list = []

replace_punc = ['-',
                "'",
                ',',
                '.',
                ')',
                '(',
                '"',
                '?',
                ';',
                '\n']

# Put the input file into a list,(by char)


with open('./sherlock.txt', 'r') as f_input:
    raw_input_list = list(f_input.read())

# Build up an input list with unwanted punctuation replaced
for i, x in enumerate(raw_input_list):
    if x in replace_punc:
        input_list.append(' ')
    else:
        input_list.append(x)

# get a list of words, instead of chars
input_text = "".join(input_list)
input_list = input_text.split(" ")
# print(input_list)

# Create the trigram from the cleaned up input
trigram = {}
# we need a pair hence the len(input_list) - 2 instead of len(input_list) - 1
for i in range(len(input_list) - 2):
    # must be a tuple in order to be a key in trigram
    trigram_key = tuple(input_list[i:i + 2])
    trigram_value = input_list[i + 2]
    # this is so nifty, I had to use it
    trigram.setdefault(trigram_key, []).append(trigram_value)

# Build the text output.text
# Start with a random word from the trigram

random_number = random.randrange(0, len(trigram) - 1)
for i, j in enumerate(trigram):
    if i == random_number:
        initial_trigram_key = j
        break

output_list = list(j) + trigram[j]
while(True):
    # Next keyword pair = last two elements of output_list
    new_key = tuple(output_list[-2:])
    try:
        trigram_value_list = trigram[new_key]
    except KeyError:
        # pick a random word in trigram_value_list
        print('exiting')
        break
    random_trigram_value = random.choice(trigram_value_list)
    new_value = random_trigram_value
    output_list = output_list + list(new_key) + [new_value]
    if len(output_list) > 2500:
        break
t = " ".join(output_list)
# print(t)
with open('trigrams.txt', 'w') as f_output:
    f_output.write(t)
