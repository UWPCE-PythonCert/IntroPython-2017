from random import choice

infile = 'sherlock.txt'
text = []
trigrams = {}
# open file and build a list of all the words
with open(infile) as f:
    for lines in f:
        text += lines.strip().split(' ')


def get_trigrams(words):
    """create the trigrams from the infile"""
    for i in range(len(words) - 2):
        pair = tuple(words[i: i + 2])
        follower = [words[i + 2]]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]


def get_new_text(wordpair):
    """take a key from the trigram dic and build the new block of text"""
    wordpair = tuple(wordpair)
    new_text = []
    blocktext = ''
    while wordpair in trigrams:
        new_text.append(choice(trigrams[wordpair]))
        wordpair = (wordpair[-1], new_text[-1][-1])
    for i in range(len(new_text)):
        blocktext += new_text[i][0] + ' '
    print(blocktext)


if __name__ == "__main__":
    # get_trigrams('I wish I may I wish I might'.split(' '))
    # get_new_text(('I', 'wish'))
    get_trigrams(text)
    get_new_text(choice(list(trigrams)))
    # get_new_text(trigrams.get())
