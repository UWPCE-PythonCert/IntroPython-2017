#! /usr/bin/env python

"""
This scripts takes as input a text file named sherlock.txt
The output is trigrams.txt text file.

The set of data will be in the form of a trigram created as follows:
         Look at each set of three adjacent words in a document.
         Use the first two words of the set as a key, and remember
         the fact that the third word followed that key.
         So the trigram will look like:
         {(word1, word2): [word3, next_word, ...],
         (word2, word3): [list of words that follow word2 and word3], ...}.
         To get the next_word value, search the text for all words that follow
         word1 and word2 pair.

 To generate the output text file from the trigram,
         choose an arbitrary word pair from the dict as a starting point.
 Use this pair to look up a random next word (using the trigram above) and
           append this new word to the output file.
 This now gives a new word pair at the end of the output file.
 Look up a potential next word, using the trigram, based on these.
 Add this to the output file, and so on.
 Eventually the potential next word won't be in the trigram.
 At this point this script will write the final output
 The final output file will be a mutated form of the input text file.
 """
import random

# raw_input_list = []
input_list = []
# initial_trigram_key = tuple()
# output_list = []

# List of chars to remove or replace with a space from input text
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


def replace_unwanted_punctuation(raw_input_list, replace_punc):
    """ Build up an input list with unwanted punctuation replaced
    :param1 = a list of char with punctuation
    :param2 = a list of char unwanted punctuation
    :return a list of char free of unwanted punctuation
    """
    for i, x in enumerate(raw_input_list):
        if x in replace_punc:
            input_list.append(' ')
        else:
            input_list.append(x)
    return input_list


def create_the_trigram(input_list):
    """ Create a trigram from a list.
    :param1 = a list
    :return = a dictionary, (trigram)
    """
    trigram = {}
    # we need a pair hence the len(input_list) - 2
    #   instead of len(input_list) - 1
    for i in range(len(input_list) - 2):
        # must be a tuple in order to be a key in trigram
        trigram_key = tuple(input_list[i:i + 2])
        trigram_value = input_list[i + 2]
        # this is so nifty, I had to use it
        trigram.setdefault(trigram_key, []).append(trigram_value)
    return trigram


def initial_output_list(trigram):
    """Initialize the output list with three elements derived from a
    random trigram key
    :param = dictionary, (trigram)
    :return list
    """
    random_number = random.randrange(0, len(trigram) - 1)
    for i, j in enumerate(trigram):
        if i == random_number:
            initial_trigram_key = j
            break
    output_list = list(initial_trigram_key) + trigram[initial_trigram_key]
    return output_list


if __name__ == "__main__":
    with open('./sherlock.txt', 'r') as f_input:
        raw_input_list = list(f_input.read())

    # Clean up the input
    input_list = replace_unwanted_punctuation(raw_input_list, replace_punc)

    # get a list of words, instead of chars
    input_text = "".join(input_list)
    input_list = input_text.split(" ")

    # Create the trigram from the cleaned up input
    trigram = create_the_trigram(input_list)

    # Build the text output.text
    # Start with a random word from the trigram

    output_list = initial_output_list(trigram)

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
