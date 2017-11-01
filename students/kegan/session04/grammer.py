"""
Kathryn Egan

Uses ngrams to produce a randomly-generated text based off
of user-provided input text. User specifies length of ngram.
Output is written to a text of the same name as the input with
the ngram type:

[input_file]_output_[uni|bi|tri|quadri]gram.txt

Ngrams are written to a separate file:

[input_file].[uni|bi|tri|quadri]grams

Text is initially stripped of any punctuation that is not desired
in the text, then tokenized on whitespace. All numbers and certain
punctuation are stripped from the beginning and end of each token.
Other punctuation and newlines are preserved. Clause- or sentence-
ending punctuation/newlines are treated as tokens.

Titles such as Mrs., Mr., etc. are preserved with the following name.

Assumes that the correct format for any given string is the
format that most frequently occurs in the text. Author is aware
of how this may fail but implementing a more complicated method
is outside the scope of this task.

The program tracks which n-1grams start a sentence and only uses
those n-1grams to start sentences.

Otherwise, all n-1grams and final tokens to complete the ngram
are randomly chosen, in effect weighted by their frequency in source text.

If any chosen ngram results in a failure of the program to choose
the next n-1gram, then the previous choice is repeated until success.

Ensures program will not hang by enforcing a period at the end of
the text.
"""
import sys
import argparse
from random import randint


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('n', help='number of grams, 2-4', type=int)
    parser.add_argument(
        'sentences', type=int, help='number of sentences in output, 1-500')
    args = parser.parse_args()
    check_args(args)
    text = read_text(args.input_file)
    text = snip_gutenberg(text)
    tokens = tokenize(text, args.n)
    ngrams, starters = generate_ngrams(tokens, args.n)
    output = generate_output(ngrams, starters, args.n, args.sentences)
    output = textify(output)
    ngrams = ngrams_to_string(ngrams)
    write_output(args, output)
    write_ngrams(args, ngrams)


def check_args(args):
    """ Check command line arguments to ensure they are valid.
    Args:
        args (ArgumentParser) : parsed arguments from command line
    """
    # check that num sentences is 1-500
    if 1 > args.sentences or args.sentences > 500:
        sys.exit('ERROR: Number of sentences must be between 1 and 500')
    # check that n is 2-4
    if 2 > args.n or args.n > 4:
        sys.exit('ERROR: Number of grams must be between 2 and 4')


def read_text(input_file):
    # read in text, tokenize, ngramize, produce output, write to file
    sys.stderr.write('Reading in {}...\n'.format(input_file))
    try:
        with open(input_file, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        sys.exit('ERROR: {} not found'.format(input_file))
    return text


def write_output(args, output):
    """ Writes output to output file
    Args:
        args (ArgumentParser) : arguments from command line
        output (str) : output as string
    """
    output_file = '_'.join([args.input_file[:-4], 'random', '{}grams'])
    output_file = output_file.format(args.n) + '.txt'
    sys.stderr.write('Writing output to {}...\n'.format(output_file))
    with open(output_file, 'w') as f:
        f.write(output)


def write_ngrams(args, ngrams):
    """ Writes ngrams to ngram file
    Args:
        args (ArgumentParser) : arguments from command line
        ngrams (str) : ngrams as string
    """
    ngram_file = args.input_file[:-4] + '.{}grams'.format(args.n)
    sys.stderr.write('Writing ngrams to {}...\n'.format(ngram_file))
    with open(ngram_file, 'w') as f:
        f.write(ngrams)


def snip_gutenberg(text):
    """ Hacky way to emove Gutenberg's legal and publishing
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


def tokenize(text, n):
    """ List-based sentence tokenization. Tokenizes
    words by whitespace, splits and tokenizes select
    punctuation, removes numbers. Retains paragraphs
    by replacing double new lines with distinct token.
    Joins titles with following token in order to retain format.
    Args:
        text (str) : text to tokenize
    Returns:
        results (list of str) : tokens in text
        propers (set of str) : proper names
    """
    sys.stderr.write('Tokenizing text...\n')
    text = remove_forbidden(text)
    text = text.split()
    tokens = []
    formats = {}
    index = 0
    title = ''
    for index, token in enumerate(text):
        token = trim_characters(token)
        title, token = get_title(title, token)
        token, punctuation = split_punctuation(token)
        lowtoken = token.lower()
        tokens.extend([t for t in [lowtoken, punctuation] if t])
        if lowtoken not in formats:
            formats[lowtoken] = {}
        if token not in formats[lowtoken]:
            formats[lowtoken][token] = 0
        formats[lowtoken][token] += 1
    formats = get_formats(formats)
    # reformat each token according to its commonest format
    tokens = [formats[t] if t in formats else t for t in tokens]
    if len(tokens) < n:
        message =\
            'ERROR: Text must have at least {} ' +\
            'tokens in it to generate {}grams'
        sys.exit(message.format(n, n))
    # Enforce well-formed text
    if tokens and tokens[-1] not in ('?', '!', '.'):
        tokens.append('.')
    return tokens


def get_formats(formats):
    """ Returns lowered string to its most common upper
    and lower case format in original text.
    Args:
        formats (dic str:str:count) :
            normalized token mapped to various formats and their counts
    Returns:
        dic (str:str) : normalized token mapped to most frequent format
    """
    common_format = {}
    for token in formats:
        common = max(formats[token].items(), key=lambda item: item[1])[0]
        common_format[token] = common
    return common_format


def get_title(title, token):
    """ Returns current applicable title for next token, and current token.
    Args:
        title (str) : current title
        token (str) : current token
    Returns:
        title (str) :
            title if current token is a title, otherwise empty string
        token (str) : current token, which may be joined with a title
    """
    titles = (
        'Mrs', 'Mr', 'Lady', 'Sir', 'Dr', 'Ms',
        'Miss', 'Missus', 'Misses', 'Mister')
    # current token is a title, update title tracker and reset token
    if token.strip('.') in titles:
        title = token
        token = ''
    # previous token was a title so join this
    # token to previous and reset title
    elif token and title:
        token = title + '_' + token
        title = ''
    return title, token


def remove_forbidden(text):
    """ Removes forbidden characters from text
    that may not be detected through tokenization
    methods.
    Args:
        text (str) : text to update
    Returns:
        str : updated text
    """
    forbidden = ('\n', '--', '_', '(', ')')
    text = text.replace('\n\n', ' newparagraph ')
    for f in forbidden:
        text = text.replace(f, ' ')
    return text


def trim_characters(token):
    """ Trims unwanted puncuation and characters
    from given token.
    Args:
        token (str) : token to trim
    Returns:
        str : trimmed token
    """
    while token and not is_allowed(token[0]):
        token = token[1:]
    while token and not is_allowed(token[-1]):
        token = token[:-1]
    return token


def split_punctuation(token):
    """ Splits final punctuation from the given
    token and returns separately.
    Args:
        token (str) : token to split
    Returns:
        token (str) : token without final punctuation
        punctuation (str) : final punctuation, empty string if none
    """
    punctuation = ''
    if token and is_punctuation(token[-1]):
        punctuation = token[-1]
        token = token[:-1]
    return token, punctuation


def is_allowed(char):
    """ Returns whether the given character is allowed in text.
    Args:
        char (str) : character to evaluate
    Returns:
        bool : True if character is allowed, False otherwise
    """
    return char.isalpha() or is_punctuation(char)


def is_punctuation(char):
    """ Returns true if the character is a type of allowed
    punctuation.
    Args:
        char (str) : character to evaluate
    Returns:
        bool : True if character is allowed punctuation, False otherwise
    """
    return char in ('\\', '?', '!', ':', ';', '.', ',')


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
    sys.stderr.write('Generating {}grams...\n'.format(n))
    ngrams = {}
    starters = []
    for index, token in enumerate(tokens):
        if index > len(tokens) - n:
            break
        n_1gram = tuple(tokens[index:index + n - 1])
        endgram = tokens[index + n - 1]
        ngrams.setdefault(n_1gram, [])
        ngrams[n_1gram].append(endgram)
        # assumes preceding period means start of sentence
        if index == 0 or tokens[index - 1] == '.':
            starters.append(n_1gram)
    return ngrams, starters


def ngrams_to_string(ngrams):
    """ Returns given ngrams as a pretty-printed sting.
    Args:
        ngrams (dic tuple:list) : n-1gram mapped to list of final tokens
    Returns:
        str : pretty-printed ngrams
    """
    stringrams = []
    for n_1gram in sorted(ngrams):
        stringrams.append('_'.join(n_1gram))
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
    sys.stderr.write('Generating output...\n')
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
        if not is_punctuation(n_1gram[0]) and not n_1gram[0] == 'newparagraph':
            break
    endgram = choose_random(ngrams[n_1gram])
    output.extend(n_1gram)
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


def choose_random(elements):
    """ Chooses a random element from a given list of elements.
    Args:
        elements (list) : list of elements to choose from
    Returns:
        value : random element from list
    """
    return elements[randint(0, len(elements) - 1)]


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
        token = token.replace('newparagraph', '\n\n')
        token = token.replace('_', ' ')
        # remove preceding whitespace when token is a type of punctuation
        output = output[:-1] if is_punctuation(token) else output
        token = \
            token.capitalize()\
            if capital(start, prev, token) else token
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
    cap_next = ('.', '?', '!', '\n\n')
    return start or prev in cap_next


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
