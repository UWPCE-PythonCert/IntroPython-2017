'''Test for BaseLinter'''

import json
import os
import datetime
import mock
import baselinter.baselinter as BS

def test_open_set_json():
    '''Function returns a list of sets from a json file.'''
    list_of_sets = BS.open_set_json(os.path.dirname(BS.__file__) + "\\test\\dummy-data.json")

    assert {"mole","vole"} == list_of_sets[0]

def test_text_to_list():
    '''Function returns from a filename a list of words in order.'''
    wordlist = BS.text_to_list(os.path.dirname(BS.__file__) + "\\test\\dummy-text.txt")

    assert len(wordlist) == 413
    assert wordlist[0] == "We"
    assert wordlist[20] == "climbed"

def test_wordlist_to_text():
    '''Function returns from a list of words in order a single string.'''
    test_list = ['We', 'got', 'up', 'at', 'four', 'in', 'the', 'morning,', 'that', 'first', 'day', 'in', 'the', 'east.']
    out_text = BS.wordlist_to_text(test_list)
    
    assert out_text == "We got up at four in the morning, that first day in the east."


def test_return_members():
    '''Function returns the set of an item if a member of the set, otherwise returns None.'''
    test_set = [{"that1", "that2", "that3"},{"mole", "vole"}]

    assert BS.return_members(test_set, "mole") == {"mole", "vole"}
    assert BS.return_members(test_set, "fig") == None

def test_select_update():
    '''Function returns an updated list'''
    assert True