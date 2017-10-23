"""
Kathryn Egan

Uses ngrams to produce a randomly-generated text based off
of user-provided input text. User specifies length of ngram
and can provide a feeder n-1gram that the program will use
to start text.

All numbers and certain punctuation are stripped from input text.
Other punctuation and newlines are preserved.

Beginnings of sentences and the pronoun I are capitalized, otherwise
nothing is capitalized.

Titles such as Mrs., Mr., etc. are stripped of periods and
kept with the following token in an attempt to preserve names.

The program tracks which n-1grams start a sentence and only uses
those n-1grams to start sentences.

Otherwise, all n-1grams and final tokens to complete the ngram
are randomly chosen.

If any chosen ngram results in a failure of the program to choose
the next n-1gram, then the sentence is ended with an ellipses and
a new paragraph is started.
"""
import argparse
from random import randint
from datetime import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('n', help='number of grams, 2-6', type=int)
    parser.add_argument(
        'sentences', type=int, help='number of sentences in output, 1-500')
    parser.add_argument(
        '-f', '--feeder', help='csv n_1gram to feed the grammer (optional)')
    args = parser.parse_args()

    # check that num sentences is 1-500
    if 1 > args.sentences > 500:
        print('Number of tokens must be between 1 and 500')
        return
    # check that n is 2-4
    if 2 > args.n > 6:
        print('Number of grams must be between 2 and 6')
        return
    # check that feeder is viable n-1gram
    feeder = None
    if args.feeder:
        feeder = tuple(args.feeder.lower().split(','))
    if feeder and len(feeder) != args.n - 1:
        message = 'Passed feeder is length {}. Must pass feeder of length {}.'
        print(message.format(len(feeder), args.n - 1))
        return

    # read in text, tokenize, ngramize, produce output, write to file
    with open(args.input_file, 'r') as f:
        text = f.read()
    text = snip_gutenberg(text)
    tokens = tokenize(text)
    ngrams = generate_ngrams2(tokens, args.n)
    stringrams = ngrams_to_string(ngrams)
    # write ngrams for given text to file
    with open(args.input_file[:-4] + '_{}grams.txt'.format(args.n), 'w') as f:
        f.write(stringrams)
    # check whether the feeder n-1gram is in ngrams
    if feeder and feeder not in set(ngrams[True].keys()).union(ngrams[False]):
        print('Feeder not found. Try again.')
        return
    output = generate_output(ngrams, args.n, args.sentences, feeder)
    output = textify(output)
    print(output)
    return
    # write output to file
    filename = args.input_file[:-4] + '_' + str(datetime.today()) + '.txt'
    with open(filename, 'w') as f:
        f.write(output)


def snip_gutenberg(text):
    """ Removes Gutenberg's legal and publishing
    header/footer from text if it exists.
    Args:
        text (str) : text to modify
    Returns:
        str : modified text
    """
    modified = []
    collect = False
    gutenberg = False
    for line in text.split('\n'):
        if line.startswith('***START') or line.startswith('*** START'):
            collect = True
            gutenberg = True
            continue
        elif line.startswith('***END') or line.startswith('*** END'):
            collect = False
            continue
        if collect:
            modified.append(line)
    if gutenberg:
        return '\n'.join(modified)
    return text


def tokenize(text):
    """ List-based sentence tokenization. Tokenizes
    words by whitespace, splits and tokenize select
    punctuation, removes numbers and other punctuation.
    Retains paragraphs by replacing double new lines with token.
    Distinguishes titles from period punctuation and joins
    with following token in order to retain title format.
    Args:
        text (str) : text to tokenize
    Returns:
        list of str : tokens in text
    """
    titles = {
        'mrs.': 'mrs',
        'misses': 'misses',
        'mr.': 'mr',
        'mister': 'mister',
        'ms.': 'ms',
        'miss': 'miss',
        'lady': 'lady',
        'sir': 'sir',
        'dr.': 'dr'}
    text = text.strip().lower()
    text = text.replace('\n\n', ' \\newline ')
    for title, replacement in titles.items():
        text = text.replace(title + ' ', replacement + '\\title')
    results = []
    for index in range(len(text)):
        char = text[index]
        # replace unwanted chars with whitespace
        if not char.isalpha() and not punctuation(char):
            results.append(' ')
        # split clause-ending punctuation from preceding token
        elif punctuation(char, clause=True):
            results.append(' ')
            results.append(char)
        # keep if ' is apostrophe, remove if single quotation mark
        elif char == '\'':
            start = index - 1
            end = index + 1
            startalpha = False if start < 0 else text[start].isalpha()
            endalpha = False if end > len(text) - 1 else text[end].isalpha()
            # single quotation mark has non alpha on one side
            # will also inadvertently lose apostrophes on plurals
            if not startalpha or not endalpha:
                results.append(' ')
            else:
                results.append(char)
        # char is alpha
        else:
            results.append(char)
    results = ''.join(results)
    results = results.split()
    return results


def punctuation(char, clause=False):
    """ Returns whether the given character is ALLOWED
    punctuation for tokenization process.
    Args:
        char (str) : character to evaluate
        quote (bool) :
            True if evaluation should include single quote
            False otherwise
    Returns:
        bool :
            True if character is an allowed form of punctuation
            False otherwise
    """
    clause_punc = ['?', '!', '.', ',', ':', ';']
    mid = ['\\', '\'']
    return char in clause_punc if clause else char in clause_punc + mid


def generate_ngrams(tokens, n):
    """ Generates ngrams of length n as an n-1gram
    tuple mapped to list of all possible final tokens in ngram.
    Args:
        tokens (list of str) : list of tokens
        n (int) : length of ngram
    Returns:
        dic (tuple:list) : n-1gram mapped to list of all final tokens
    """
    ngrams = {}
    for index in range(len(tokens) - n + 1):
        n_1gram = tuple(tokens[index:index + n - 1])
        endgram = tokens[index + n - 1]
        ngrams.setdefault(n_1gram, [])
        ngrams[n_1gram].append(endgram)
    return ngrams


def generate_ngrams2(tokens, n):
    """ Generates ngrams of length n as an n-1gram
    tuple mapped to list of all possible final tokens in ngram.
    Args:
        tokens (list of str) : list of tokens
        n (int) : length of ngram
    Returns:
        dic (tuple:list) : n-1gram mapped to list of all final tokens
    """
    ngrams = {}
    for index in range(len(tokens) - n + 1):
        n_1gram = tuple(tokens[index:index + n - 1])
        start = tokens[index - 1] == '.'
        endgram = tokens[index + n - 1]
        ngrams.setdefault(start, {})
        ngrams[start].setdefault(n_1gram, [])
        ngrams[start][n_1gram].append(endgram)
    return ngrams


def generate_ngrams3(tokens, n):
    """ Generates ngrams of length n as an n-1gram
    tuple mapped to final token in ngram.
    Args:
        tokens (list of str) : list of tokens
        n (int) : length of ngram
    Returns:
        dic (tuple:str) : n-1gram mapped to final token
    """
    ngrams = {}
    # create unigrams through ngrams
    for gram_length in range(1, n + 1):
        ngrams.setdefault(gram_length, {})
        for index in range(len(tokens) - gram_length + 1):
            n_1gram = tuple(tokens[index:index + gram_length - 1])
            endgram = tokens[index + gram_length - 1]
            ngrams[gram_length].setdefault(n_1gram, [])
            ngrams[gram_length][n_1gram].append(endgram)
    return ngrams


def choose_random(elements):
    """ Chooses a random element from a given list of elements.
    Args:
        elements (list) : list of elements to choose from
    Returns:
        value : random element from list
    """
    return elements[randint(0, len(elements) - 1)]


def ngrams_to_string(ngrams):
    """ Returns given ngrams as a pretty-printed sting.
    Args:
        dic (tuple:list) : n-1gram mapped to list of final tokens
    Returns:
        str : pretty-printed ngrams
    """
    stringrams = []
    for bool in ngrams:
        stringrams.append(str(bool) + '\n')
        for n_1gram in sorted(ngrams[bool]):
            stringrams.append(', '.join(n_1gram))
            for endgram in sorted(ngrams[bool][n_1gram]):
                stringrams.append('\t' + endgram)
            stringrams.append('')
    stringrams = '\n'.join(stringrams)
    return stringrams


def generate_output(ngrams, n, sentences, feeder):
    """ Generates given number of sentences using ngrams
    and feeder n-1gram if provided. The feeder n-1gram is a user-specified
    n_1gram that the program will use to generate the first sentence.
    Args:
        ngrams (dic tuple:list) : n-1grams mapped to list of final tokens
        n (int) : length of ngram
        sentences (int) : number of sentences to produce
        feeder (tuple) : user-specified first n-1 gram
    Returns:
        list of str : tokens generated using ngrams
    """
    output = []
    cursor = 1
    count = 0
    while True:
        # initialize output with feeder if given
        if not output:
            output = initialize(output, ngrams, feeder)
        # initialize a new sentence with a random n-1gram
        elif output[-1].startswith('.'):
            count += 1
            if count == sentences:
                return output
            output = initialize(output, ngrams, feeder=None)
            # adjust cursor to point to end of new n_1gram
            cursor = len(output) - n + 1
        # choose next random endgram in sentence given n_1gram
        else:
            n_1gram = tuple(output[cursor:cursor + n])
            try:
                endgram = choose_random(list(ngrams[False][n_1gram]))
            except KeyError:
                endgram = '...\n\n'
            output.append(endgram)
            cursor += 1


def initialize(output, ngrams, feeder):
    """ Initializes sentence with feeder if given, otherwise
    randomly-chosen ngram.
    Args:
        output (list of str) : current list of tokens
        ngrams (dic tuple:list) : n-1grams mapped to list of final tokens
        feeder (tuple) : user-specified first n-1 gram
    Returns:
        list of str : updated list of tokens
    """
    if feeder:
        n_1gram = feeder
        try:
            endgram = choose_random(ngrams[True][n_1gram])
        except KeyError:
            endgram = choose_random(ngrams[False][n_1gram])
    else:
        # never begin sentence with punctuation or new paragraph
        while True:
            n_1gram = choose_random(list(ngrams[True]))
            if not punctuation(n_1gram[0]) and not n_1gram == 'newline':
                break
        endgram = choose_random(ngrams[True][n_1gram])
    for token in n_1gram:
        output.append(token)
    output.append(endgram)
    return output


def textify(tokens):
    """ Formats the given tokens and returns them as text.
    Args:
        tokens (list of str) : tokens to format
    Returns:
        str : formatted tokens as string
    """
    capitalized = ['i', 'i\'ll', 'i\'d']
    output = []
    prev = ''
    start = True
    for token in tokens:
        # replaces newline token with double new line
        if token == '\\newline':
            token = '\n\n'
            output.append(token)
            prev = token
            continue
        if '\\title' in token:
            title, name = token.split('\\title')
            for element in token.split('\\title'):
                output.append(element)
                output.append(' ')
            prev = token
            continue
        # capitalize pre-specified words or words starting new sentences
        if start or prev in ('.', '?', '!', '\n\n') or token in capitalized:
            token = token.capitalize()
            start = False
        # remove preceding whitespace when token is a type of punctuation
        if punctuation(token):
            output = output[:-1]
        prev = token
        output.append(token)
        output.append(' ')
    output = ''.join(output).strip()
    return output


if __name__ == '__main__':
    main()
