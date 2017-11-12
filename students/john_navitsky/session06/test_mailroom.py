#!/usr/bin/env python3

import mailroom
import pytest
import io


def test_true():
    assert True


def test_parse_name():
    assert mailroom.parse_name("Mary Jo Smith, IV") == {
        'full_name': 'Mary Jo Smith, Iv', 
        'informal_name': 'Mary Jo Smith',
        'suffix': 'IV',
        'last_name': 'Smith',
        'first_name': 'Mary Jo' }


def test_print_lines():
    # verify the print_lines() function
    out = io.StringIO()
    mailroom.print_lines(3,out)
    output = out.getvalue()
    out.close()
    assert output == "\n\n\n"


def test_mock_input():
    # verify our mock input works
    assert mailroom.safe_input(mock=True,mock_in="foo") == "foo"


# def test_print_thank_you():
#      # verify the print_thank_you() function
#     out = io.StringIO()
#     mailroom.print_thank_you(0,"testfull",out)
#     output = out.getvalue()
#     out.close()
#     assert "Dearest Joe Smith," in output


