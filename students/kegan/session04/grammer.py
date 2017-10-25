"""
Kathryn Egan

Uses ngrams to produce a randomly-generated text based off
of user-provided input text. User specifies length of ngram.

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    parser.add_argument('n', help='number of grams, 2-6', type=int)
    parser.add_argument(
        'sentences', type=int, help='number of sentences in output, 1-500')
    args = parser.parse_args()

    # check that num sentences is 1-500
    if 1 > args.sentences > 500:
        print('Number of tokens must be between 1 and 500')
        return
    # check that n is 2-4
    if 2 > args.n > 6:
        print('Number of grams must be between 2 and 6')
        return

    # read in text, tokenize, ngramize, produce output, write to file
    with open(args.input_file, 'r') as f:
        text = f.read()
    text = snip_gutenberg(text)
    tokens = tokenize(text)
    if not tokens:
        print('Text in {} is not suitable.'.format(args.input_file))
        return
    ngrams, starters = generate_ngrams(tokens, args.n)
    # write ngrams for given text to file
    ngram_file = args.input_file[:-4] + '_{}grams.txt'.format(args.n)
    with open(ngram_file, 'w') as f:
        f.write(ngrams_to_string(ngrams, starters))
    output = generate_output(ngrams, starters, args.n, args.sentences)
    output = textify(output)
    print(output)
    return
    # write output to file
    with open(args.output_file, 'w') as f:
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
        elif line.startswith('***END') or line.startswith('*** END'):
            collect = False
        elif collect:
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
    text = text.strip().lower()
    text = text.replace('\n\n', ' \\newline ')
    text = join_title_name(text)
    results = []
    index = 0
    # while loop allows free incrementing index
    while index < len(text):
        char = text[index]
        if char.isnumeric():
            # skip over any numeric characters including
            # any sequential alpha characters
            while text[index].isalnum() and index < len(text):
                index += 1
            continue
        # keep alpha characters and backslashes
        if char.isalpha() or char == '\\':
            results.append(char)
        # split clause-ending punctuation from preceding token
        elif clause_punctuation(char):
            results.append(' ')
            results.append(char)
        # keep in-word apostrophes, remove single quotation marks
        elif apostrophe(text, index, char):
            results.append(char)
        # replace all other characters with whitespace
        else:
            results.append(' ')
        index += 1
    results = ''.join(results).strip()
    results = results.split()
    return results


def join_title_name(text):
    """ Replaces periods and whitespace intervening
    a title and a name with \\title to preserve
    title + name combo.
    Args:
        text (str) : text to use
    Returns:
        str : text with titles and names joined
    """
    # ordered tuple to preserve order of operations
    titles = (
        ('mrs.', 'mrs'),
        ('mrs', 'mrs'),
        ('misses', 'misses'),
        ('mr.', 'mr'),
        ('mr', 'mr'),
        ('mister', 'mister'),
        ('ms.', 'ms'),
        ('ms', 'ms'),
        ('miss', 'miss'),
        ('lady', 'lady'),
        ('sir', 'sir'),
        ('dr.', 'dr'),
        ('dr', 'dr'))
    for title, replacement in titles:
        in_string = ' ' + title + ' '
        out_string = ' ' + replacement + '\\title'
        text = text.replace(in_string, out_string)
    return text


def apostrophe(text, index, char):
    """ Returns whether the apostrophe at the given index
    is a single quote (vs. apostrophe). This is determined
    by examining whether the leading or following character
    is not alpha. Will erroneously count plural apostrophes
    as single quotes.
    Args:
        text (str) : text to evaluate
        index (int) : index of apostrophe
    Returns:
        bool :
            True if character is singe quote
            False if character is apostrophe
    """
    if char not in ('\'', '’'):
        return False
    start = index - 1
    end = index + 1
    startalpha = False if start < 0 else text[start].isalpha()
    endalpha = False if end > len(text) - 1 else text[end].isalpha()
    return startalpha and endalpha


def single_quote(char):
    """ Returns whether given character is a single quote symbol.
    Args:
        char (str) : character to evaluate
    Returns:
        bool : True if character is single quote, False otherwise
    """
    return char in ('\'', '’')


def punctuation(char):
    """ Returns whether the given character is ALLOWED
    punctuation for tokenization process.
    Args:
        char (str) : character to evaluate
    Returns:
        bool :
            True if character is an allowed form of punctuation
            False otherwise
    """
    return char == '\\' or clause_punctuation(char) or single_quote(char)


def clause_punctuation(char):
    """ Returns whether given character is a form of
    clause-ending punctuation.
    Args:
        char (str) : character to evaluate
    Returns:
        bool :
            True if character is a clause-ending punctuation
            False otherwise
    """
    return char in ('?', '!', '.', ',', ':', ';')


def generate_ngrams(tokens, n):
    """ Generates ngrams of length n as an n-1gram
    tuple mapped to list of all possible final tokens in ngram.
    Generates a list of n-1grams that start sentences.
    Args:
        tokens (list of str) : list of tokens
        n (int) : length of ngram
    Returns:
        ngrams (dic tuple:list) : n-1gram mapped to list of all final tokens
        starters (list of tuple) : list of n-1grams that start sentences
    """
    ngrams = {}
    starters = []
    for index in range(len(tokens) - n + 1):
        n_1gram = tuple(tokens[index:index + n - 1])
        endgram = tokens[index + n - 1]
        ngrams.setdefault(n_1gram, [])
        ngrams[n_1gram].append(endgram)
        # assumes preceding period means start of sentence
        if tokens[index - 1] == '.':
            starters.append(n_1gram)
    return ngrams, starters


def ngrams_to_string(ngrams, starters):
    """ Returns given ngrams as a pretty-printed sting.
    Args:
        ngrams (dic tuple:list) : n-1gram mapped to list of final tokens
        starters (list of tuple) : list of n-1grams that start sentences
    Returns:
        str : pretty-printed ngrams
    """
    stringrams = []
    for n_1gram in sorted(ngrams):
        stringrams.append('_'.join(n_1gram))
        if n_1gram in starters:
            stringrams.append('*STARTER*')
        for endgram in sorted(ngrams[n_1gram]):
            stringrams.append('\t' + endgram)
        stringrams.append('')
    stringrams = '\n'.join(stringrams)
    return stringrams


def generate_output(ngrams, starters, n, sentences):
    """ Generates given number of sentences using ngrams.
    Args:
        ngrams (dic tuple:list) : n-1grams mapped to list of final tokens
        starters (list of tuple) : list of n-1grams that start sentences
        n (int) : length of ngram
        sentences (int) : number of sentences to produce
    Returns:
        list of str : tokens generated using ngrams
    """
    output = []
    count = 0
    while True:
        # initialize a new sentence with a random n-1gram
        if not output or output[-1] in ('.', '...'):
            count += 1
            if count == sentences:
                return output
            output = initialize(output, ngrams, starters)
        # choose next random endgram in sentence given n_1gram
        else:
            output = get_next(output, ngrams, n)


def choose_random(elements):
    """ Chooses a random element from a given list of elements.
    Args:
        elements (list) : list of elements to choose from
    Returns:
        value : random element from list
    """
    return elements[randint(0, len(elements) - 1)]


def initialize(output, ngrams, starters):
    """ Initializes sentence with feeder if given, otherwise
    randomly-chosen ngram.
    Args:
        output (list of str) : current list of tokens
        ngrams (dic tuple:list) : n-1grams mapped to list of final tokens
        starters (list of tuple) : list of n-1grams that start sentences
    Returns:
        list of str : updated list of tokens
    """
    while True:
        n_1gram = choose_random(starters)
        # never begin sentence with punctuation or new paragraph
        if not punctuation(n_1gram[0]) and not n_1gram[0] == '\\newline':
            break
    endgram = choose_random(ngrams[n_1gram])
    for token in n_1gram:
        output.append(token)
    output.append(endgram)
    return output


def get_next(output, ngrams, n):
    """ Initializes sentence with feeder if given, otherwise
    randomly-chosen ngram.
    Args:
        output (list of str) : current list of tokens
        ngrams (dic tuple:list) : n-1grams mapped to list of final tokens
        n (int) : length of ngram
    Returns:
        list of str : updated list of tokens
    """
    n_1gram = tuple(output[len(output) - n + 1:len(output)])
    if n_1gram not in ngrams:
        output = output[:-1]
        n_1gram = tuple(output[len(output) - n + 1:len(output)])
    endgram = choose_random(ngrams[n_1gram])
    output.append(endgram)
    return output


def textify(tokens):
    """ Formats the given tokens and returns them as text.
    Args:
        tokens (list of str) : tokens to format
    Returns:
        str : formatted tokens as string
    """
    output = []
    prev = ''
    start = True
    for token in tokens:
        token = token.replace('\\newline', '\n\n')
        token = token.replace('\\title', ' ')
        # remove preceding whitespace when token is a type of punctuation
        output = output[:-1] if punctuation(token) else output
        token = token.capitalize() if capital(start, prev, token) else token
        start = False
        output.append(token)
        output.append(get_buffer(token))
        prev = token
    output = ''.join(output).strip()
    return output


def capital(start, prev, token):
    """ Returns True if given token should be capitalized.
    Args:
        start (bool) : start of text
        prev (str) : previous token
        token (str) : current token
    Returns:
        bool : True if token should be capitalized, False otherwise
    """
    cap_next = ('.', '?', '!', '\n\n', '\\newline')
    cap_this = ('i', 'i\'ll', 'i\'d', 'i’ll', 'i’d')
    return start or prev in cap_next or token in cap_this


def get_buffer(token):
    """ Returns appropriate following character for given token.
    Args:
        token (str) : token to assess
    Returns:
        str : buffering character post-token
    """
    if token == '...':
        return '\n\n'
    elif token == '\n\n':
        return ''
    return ' '


if __name__ == '__main__':
    main()
