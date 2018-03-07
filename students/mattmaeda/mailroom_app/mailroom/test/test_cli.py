#!/usr/bin/env python
"""
Unit tests for mailroom cli

pytest --cov=mailroom
"""

from unittest import mock
from io import StringIO
import pytest
from mailroom import cli

THANK_YOU_OUTPUT = """
Dear Matt,

Thank you for your donation of $100.00.

"""

BAD_THANK_YOU_OUTPUT = """Invalid amount 'x' entered.

Dear Matt,

Thank you for your donation of $100.00.

"""

BAD_THANK_YOU_OUTPUT2 = """Invalid amount '0.001' entered.

Dear Matt,

Thank you for your donation of $100.00.

"""

TEST_REPORT_OUTPUT = """
Donor Name                                        | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------------------------------
Matt                                               $      100.00           1        100.00
John Adams                                         $        3.00           1          3.00
Thomas Jefferson                                   $        3.00           1          3.00
John Quincy Adams                                  $        2.00           1          2.00
James Madison                                      $        2.00           1          2.00
George Washington                                  $        1.00           1          1.00



"""


def test_get_selection():
    """ test get selection """
    user_input = ["1"]
    with mock.patch("builtins.input", side_effect=user_input):
        option = cli.get_selection()
        assert option == "1"


@mock.patch('sys.stdout', new_callable=StringIO)
def test_send_thank_you(mock_stdout):
    """ test send thank you """
    user_input = ["Matt", "100"]
    with mock.patch("builtins.input", side_effect=user_input):
        cli.send_thank_you()
        assert mock_stdout.getvalue() == THANK_YOU_OUTPUT


@mock.patch('sys.stdout', new_callable=StringIO)
def test_print_report(mock_stdout):
    """ test print output """
    user_input = ["2"]
    with mock.patch("builtins.input", side_effect=user_input):
        cli.print_report()
        assert mock_stdout.getvalue() == TEST_REPORT_OUTPUT


def test_quit_program():
    """ test quit program """
    user_input = ["3"]
    with pytest.raises(SystemExit) as sys_exit:
        cli.quit_program()
    assert sys_exit.type == SystemExit
    assert sys_exit.value.code == 0


@mock.patch('sys.stdout', new_callable=StringIO)
def test_main(mock_stdout):
    """ test main function """
    with pytest.raises(SystemExit) as sys_exit:
        user_input = ["3"]
        with mock.patch("builtins.input", side_effect=user_input):
            cli.main()
    assert sys_exit.type == SystemExit
    assert sys_exit.value.code == 0


@mock.patch('sys.stdout', new_callable=StringIO)
def test_bad_send_thank_you(mock_stdout):
    """ test send thank you """
    user_input = ["Matt", "x", "100"]
    with mock.patch("builtins.input", side_effect=user_input):
        cli.send_thank_you()

    assert mock_stdout.getvalue() == BAD_THANK_YOU_OUTPUT


@mock.patch('sys.stdout', new_callable=StringIO)
def test_another_bad_send_thank_you(mock_stdout):
    """ test send thank you """
    user_input = ["Matt", "0.001", "100"]
    with mock.patch("builtins.input", side_effect=user_input):
        cli.send_thank_you()

    assert mock_stdout.getvalue() == BAD_THANK_YOU_OUTPUT2


@mock.patch('sys.stdout', new_callable=StringIO)
def test_main_bad_selection(mock_stdout):
    """ test main bad input """
    user_input = ["4", "3"]
    with mock.patch("builtins.input", side_effect=user_input):
        with pytest.raises(SystemExit) as sys_exit:
            cli.main()

        assert mock_stdout.getvalue() == "4\n" \
                                         "ERROR: Selection '4' is invalid!\n" \
                                         "3\n"
        assert sys_exit.type == SystemExit
        assert sys_exit.value.code == 0
