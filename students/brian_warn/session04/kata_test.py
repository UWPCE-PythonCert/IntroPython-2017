#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# Kata Fourteen
import random


def main():
    exceptions = ['.', '?', ' ', '!', ',', '-']

    def build_trigram(infile):
        ''' Function that builds the trigram dictionary from the source file. '''

        trigrams = {}
        with open(infile) as sherlock:
            sherlock.readline()
            for line in sherlock:
                line = line.rstrip('\r\n')
                word = line.split(" ")
                for i in range(len(word) - 2):
                    pair = tuple(word[i:i + 2])
                    follower = word[i + 2]
                    if follower not in exceptions:
                        pass
                    # Find dictionary method that does this in one call
                    if pair in trigrams:
                        trigrams[pair].append(follower)
                    if pair not in trigrams:
                        trigrams[tuple(pair)] = [follower]

        # Check to see what's in trigrams dictionary:
        # items = trigrams.items()
        # for x in items:
        #     print(x)
        return trigrams.items()

    def get_trigram_key(trigram_items, upper):
        ''' Generates a two-word tuple. '''

        # print(trigram_items)
        len_random_choice = 1
        # Needed since some of the random_choice results may only have one word in them.  
        while len_random_choice != 2: 
            entry = []
            pattern_list = []
            # print(type(pattern_list))
            if upper == 1:
                for k, v in trigram_items:
                    if k[0][0].isupper() and k[0][-1] not in exceptions:
                        entry = [(k, v)]
                        # print("entry is: ", entry[0])
                        pattern_list.extend(entry[0])
                        # print("pattern_list is: ", pattern_list)
            else:
                for k, v in trigram_items:
                        entry = [(k, v)]
                        # print("entry is: ", entry[0])
                        pattern_list.extend(entry[0])
                        # print("pattern_list is: ", pattern_list)
            random_choice = random.choice(pattern_list)
            print("random_choice in def is: ", random_choice)
            len_random_choice = len(random_choice)
            print("random_choice length is: ", len(random_choice))
        return random_choice



    def build_sentence(trigram_items):
        ''' Construct the sentence from the trigram passed in. '''

        print("trigram_items type: ", type(trigram_items))
        # Start of sentence (i.e. upper -> 1)
        tg_key_start = get_trigram_key(trigram_items, 1)
        print("trigram key is now: ", tg_key_start)
        # Rest of sentence (i.e. upper -> 0)
        # TODO: Encapsulate in a while loop that defines when the sentence-building process is finished
        # TODO: Define the criteria that specifies how long the loop will run.
        tg_key_remaining = get_trigram_key(trigram_items, 0)
        print("rest-of-sentence trigram is: ", tg_key_remaining)


    def run_program():
        infile = "sherlock_small.txt"
        items = build_trigram(infile)
        # print("type items: ", type(items))
        # For loop to see what items contains
        # for x in items:
        #     print(x)
        # Now build the sentence
        build_sentence(items)


    run_program()

if __name__ == "__main__":
    main()
