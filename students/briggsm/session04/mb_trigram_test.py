'''
Test Trigram from:
http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
'''


import random as rand
import mb_trigram as tr

# test variables

test_infile = "text_dumb.txt"
word_list1 = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Proin', 'ultricies', 'ligula', 'et', 'diam', 'eleifend', 'placerat.', 'Aenean', 'et', 'magna', 'quis', 'nunc', 'tincidunt', 'finibus', 'ac', 'maximus', 'sem.', 'Sed', 'in', 'turpis', 'eu', 'velit', 'rhoncus', 'blandit.', 'Fusce', 'convallis', 'accumsan', 'feugiat.', 'Donec', 'est', 'odio,', 'imperdiet', 'finibus', 'sagittis', 'vel,', 'hendrerit', 'a', 'purus.', 'Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Phasellus', 'varius', 'venenatis', 'quam,', 'sed', 'ultricies', 'velit', 'pharetra', 'laoreet.']
test_trigram = {('Lorem', 'ipsum'): ['dolor', 'dolor'], ('ipsum', 'dolor'): ['sit', 'sit'], ('dolor', 'sit'): ['amet,', 'amet,'], ('sit', 'amet,'): ['consectetur', 'consectetur'], ('amet,', 'consectetur'): ['adipiscing', 'adipiscing'], ('consectetur', 'adipiscing'): ['elit.', 'elit.'], ('adipiscing', 'elit.'): ['Proin', 'Phasellus'], ('elit.', 'Proin'): ['ultricies'], ('Proin', 'ultricies'): ['ligula'], ('ultricies', 'ligula'): ['et'], ('ligula', 'et'): ['diam'], ('et', 'diam'): ['eleifend'], ('diam', 'eleifend'): ['placerat.'], ('eleifend', 'placerat.'): ['Aenean'], ('placerat.', 'Aenean'): ['et'], ('Aenean', 'et'): ['magna'], ('et', 'magna'): ['quis'], ('magna', 'quis'): ['nunc'], ('quis', 'nunc'): ['tincidunt'], ('nunc', 'tincidunt'): ['finibus'], ('tincidunt', 'finibus'): ['ac'], ('finibus', 'ac'): ['maximus'], ('ac', 'maximus'): ['sem.'], ('maximus', 'sem.'): ['Sed'], ('sem.',
'Sed'): ['in'], ('Sed', 'in'): ['turpis'], ('in', 'turpis'): ['eu'], ('turpis',
'eu'): ['velit'], ('eu', 'velit'): ['rhoncus'], ('velit', 'rhoncus'): ['blandit.'], ('rhoncus', 'blandit.'): ['Fusce'], ('blandit.', 'Fusce'): ['convallis'], ('Fusce', 'convallis'): ['accumsan'], ('convallis', 'accumsan'): ['feugiat.'], ('accumsan', 'feugiat.'): ['Donec'], ('feugiat.', 'Donec'): ['est'], ('Donec', 'est'): ['odio,'], ('est', 'odio,'): ['imperdiet'], ('odio,', 'imperdiet'): ['finibus'], ('imperdiet', 'finibus'): ['sagittis'], ('finibus', 'sagittis'): ['vel,'],
('sagittis', 'vel,'): ['hendrerit'], ('vel,', 'hendrerit'): ['a'], ('hendrerit', 'a'): ['purus.'], ('a', 'purus.'): ['Lorem'], ('purus.', 'Lorem'): ['ipsum'], ('elit.', 'Phasellus'): ['varius'], ('Phasellus', 'varius'): ['venenatis'], ('varius', 'venenatis'): ['quam,'], ('venenatis', 'quam,'): ['sed'], ('quam,', 'sed'): ['ultricies'], ('sed', 'ultricies'): ['velit'], ('ultricies', 'velit'): ['pharetra'], ('velit', 'pharetra'): ['laoreet.']}
test_index = [('Lorem', 'ipsum'), ('ipsum', 'dolor'), ('dolor', 'sit'), ('sit', 'amet,'), ('amet,', 'consectetur'), ('consectetur', 'adipiscing'), ('adipiscing', 'elit.'), ('elit.', 'Proin'), ('Proin', 'ultricies'), ('ultricies', 'ligula'), ('ligula', 'et'), ('et', 'diam'), ('diam', 'eleifend'), ('eleifend', 'placerat.'), ('placerat.', 'Aenean'), ('Aenean', 'et'), ('et', 'magna'), ('magna', 'quis'), ('quis', 'nunc'), ('nunc', 'tincidunt'), ('tincidunt', 'finibus'), ('finibus', 'ac'), ('ac', 'maximus'), ('maximus', 'sem.'), ('sem.', 'Sed'), ('Sed', 'in'), ('in', 'turpis'), ('turpis', 'eu'), ('eu', 'velit'), ('velit', 'rhoncus'), ('rhoncus', 'blandit.'), ('blandit.', 'Fusce'), ('Fusce', 'convallis'), ('convallis', 'accumsan'), ('accumsan', 'feugiat.'), ('feugiat.', 'Donec'), ('Donec', 'est'), ('est', 'odio,'), ('odio,', 'imperdiet'), ('imperdiet', 'finibus'), ('finibus', 'sagittis'), ('sagittis', 'vel,'), ('vel,', 'hendrerit'), ('hendrerit', 'a'), ('a', 'purus.'), ('purus.', 'Lorem'), ('elit.', 'Phasellus'), ('Phasellus', 'varius'), ('varius', 'venenatis'), ('venenatis', 'quam,'), ('quam,', 'sed'), ('sed', 'ultricies'), ('ultricies', 'velit'), ('velit', 'pharetra')]


def test_create_corpus():
    ''' Input: a filename of a text file
        Output: a list of words from the text file.'''
    corpus = tr.create_corpus(test_infile)
    assert corpus == word_list1


def test_create_trigram():
    ''' Input: a list of words from a text body.
        Output: a dictionary of two words in sequence and the word after.'''
    trigram = tr.create_trigram(word_list1)
    assert trigram == test_trigram


def test_get_values():
    '''Input: a dictionary.
       Output: a list of word pair keys.'''
    index = tr.get_values(test_trigram)
    assert index == test_index


def test_create_new_corpus():
    ''' Input: trigram dictionary and the trigrams list of word pairs as a list.
        Output: a list of the containing the new text.
        Note: the random text is not tested. Instead, tes if the function returns the right type of the right size.'''
    new_corpus = tr.create_new_corpus(test_trigram, test_index, 500)
    itis = type(new_corpus)
    size = len(new_corpus)
    assert itis == list
    assert size == 501


def test_create_text_from_list():
    ''' Input: A list containing the words in order. | word_list
        Output: a single string.'''
    testitem = ["This", "is", "it."]
    output = tr.create_text_from_list(testitem)
    assert output == "This is it. "

