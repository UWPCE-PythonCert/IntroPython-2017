#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# Kata Fourteen
import random
# read file and turn into a sequence of words.

# Handle any punctuation (i.e. strip out -- or keep)
# Find a pair, see what the next word that follows
# Store in a data structure.

#words = "I wish I may I wish I might".split(" ")

infile = "sherlock_small.txt"

trigrams = {}
exceptions = ['.', '?', ' ', '!', ',', '-']

with open(infile) as sherlock:
    sherlock.readline()
    for line in sherlock:
        line = line.rstrip('\r\n')
        #print(line, end=' ')
        word = line.split(" ")
        #print(word)
        for i in range(len(word) - 2):
            pair = tuple(word[i:i + 2])
            follower = word[i + 2]
            if follower not in exceptions:
                #print(pair, follower)
                pass
            # Find dictionary method that does this in one call
            #if pair in trigrams and pair[0] not in exceptions and pair[1] not in exceptions and follower not in exceptions:
            if pair in trigrams:
                #print(" pair in trigrams and follower NOT in exceptions.")
                trigrams[pair].append(follower)
            #if pair not in trigrams and pair[0] not in exceptions and pair[1] not in exceptions and follower not in exceptions:
            if pair not in trigrams:
                #print(" pair NOT in trigrams and follower NOT in exceptions.")
                trigrams[tuple(pair)] = [follower]

'''
        for i in range(len(line) - 2):
            pair = tuple(line[i:i + 2])
            follower = line[i + 2]
            if follower not in exceptions:
                #print(pair, follower)
                pass
            # Find dictionary method that does this in one call
            #if pair in trigrams and pair[0] not in exceptions and pair[1] not in exceptions and follower not in exceptions:
            if pair in trigrams:
                #print(" pair in trigrams and follower NOT in exceptions.")
                #trigrams[pair].append(follower)
                pass
            #if pair not in trigrams and pair[0] not in exceptions and pair[1] not in exceptions and follower not in exceptions:
            if pair not in trigrams:
                #print(" pair NOT in trigrams and follower NOT in exceptions.")
                trigrams[tuple(pair)] = [follower]
'''

''' Leaving the following commented-out lines here for reference.
for i in range(len(words)-2):
    pair = tuple(words[i:i+2])
    follower = words[i+2]
    print(pair, follower)
    # Find dictionary method that does this in one call
    if pair in trigrams:
        trigrams[pair].append(follower)
    else:
        trigrams[tuple(pair)] = [follower]
'''

length_trigram = len(trigrams) # Use this value for decrementing later

# Start the pattern that ultimately becomes the random-passage generator when complete.

# HELP REQUEST: How do I randomly choose the starting pattern?
#  My code here chooses the first match it encounters.

pattern = ''
pattern_list = []
for k, v in trigrams.items():
    # print("** FIRST K0:", k[0])
    if k[0][0].isupper() and k[0][-1] not in exceptions:
        pattern = pattern + ' ' + str(k[0]) + ' ' + str(k[1])
        pattern_list.extend((k[0], k[1], v[0]))
        print("**** k0: ",k[0])
        # break

raise Exception()

## Use random choice to choose the index

print("pattern is: ", pattern)
print("pattern list is: ", pattern_list)

# for x in pattern_list.items():
#     print(x)

# items = trigrams.items()
# for x in items:
#     print(x)

#print("\n\npattern is: ", pattern)
#print("key is: ", k)
#print("value is: ", v)
#pattern = pattern + ' ' + v[0]

#print("\nAppended pattern: ", pattern)
#new_key = k[1],v[0]
#print("New key is: ", new_key)
#list_length = len(trigrams[new_key])
#print("Length of new_key value is: ", list_length)
#print("Value (from list) is: ", trigrams[new_key][list_length - 1]) # <-- use random_index value during while loop.

#random_index = random.randint(0,len(trigrams[new_key][0]))
#print("random_index is: ", random_index)

# len of trigrams for sherlock_small is 144.

while length_trigram >= 1:
    '''
    1. Use key (k) to find the value.
    2. Append the value to pattern
    3. Read the last two words of pattern into a tuple.
    4. Decrement length_trigram by one and repeat the sequence starting at 1.

    '''
    #print(new_key)
    #pattern = pattern + ' ' + v[0]
    print("\nlength_trigram at top of while: ", length_trigram)
    print("Starting pattern is: ", pattern)
    print("pattern_list: ", pattern_list)
    print("pattern_list[-1]: ", pattern_list[-1])
    print("pattern_list[-2]: ", pattern_list[-2])
    next_trigram_key = (pattern_list[-2],pattern_list[-1])
    print("next_trigram_key: ", next_trigram_key)
    if next_trigram_key not in trigrams:
        print("Next trigram 'not in' next_trigram_key:", next_trigram_key)
    else:
        next_trigram_value = trigrams[next_trigram_key]
        print("next_trigram_value: ", next_trigram_value)
        list_length = len(next_trigram_key) - 1
        print("List length in while is: ", list_length)
        print("Next key is: ", next_trigram_key)
        if list_length == 1:
            random_index = 0
        else:
            random_index = random.randint(0,list_length)
            print("random_index in else: ", random_index)
        pattern_list.append(next_trigram_value[random_index])
        print("Appended pattern_list is now: ", pattern_list)
        pattern = pattern + ' ' + next_trigram_value[random_index]
        print("Sentence pattern in while is now: ", pattern)


    length_trigram -= 1
    print("length_trigram is now: ", length_trigram)
print(pattern)



