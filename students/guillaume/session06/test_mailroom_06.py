#!/usr/bin/env python3

import mailroom_06
from io import StringIO
import unittest.mock as mock
# import module

textfile = 'donors.txt'



# @mock.patch('builtins.input', side_effect=['4'])
'''
def test_leaving():
    mailroom_06.input = lambda: '4'
    mailroom_06.input_sc(textfile)
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        foo()
        output = out.getvalue().strip()
        assert output == 'Leaving Program'
    finally:
        sys.stdout = saved_stdout
'''

@mock.patch('builtins.input', side_effect=['4'])
def test_leaving():
    #with mock.patch.object(__builtin__, 'input', lambda: '4'):
    assert mailroom_06.function() == 'Leaving Program'