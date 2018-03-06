'''Test for BaseLinter'''

import json
import datetime
import mock
import baselinter as BL

def test_open_set_json():
    '''Function returns a list of sets from a json file.'''
    list_of_sets = BL.open_set_json("dummy-data.json")

    assert type(list_of_sets) == list
    assert type(list_of_sets[0]) == set
    assert list_of_sets[1] == {"mole", "vole"}

def test_text_to_list():
    '''Function returns from a filename a list of words in order.'''
    wordlist = BL.text_to_list("dummy-text.txt")

    assert len(wordlist) == 413
    assert wordlist[0] == "We"
    assert wordlist[20] == "climbed"

def test_wordlist_to_text():
    '''Function returns from a list of words in order a single string.'''
    test_list = ['We', 'got', 'up', 'at', 'four', 'in', 'the', 'morning,', 'that', 'first', 'day', 'in', 'the', 'east.']
    out_text = BL.wordlist_to_text(test_list)
    
    assert out_text == "We got up at four in the morning, that first day in the east."


def test_return_members():
    '''Function returns the set of an item if a member of the set, otherwise returns None.'''
    test_set = [{"that1", "that2", "that3"},{"mole", "vole"}]

    assert BL.return_members(test_set, "mole") == {"mole", "vole"}
    assert BL.return_members(test_set, "fig") == None

def test_select_update():
    '''Function returns an updated list'''
    assert True