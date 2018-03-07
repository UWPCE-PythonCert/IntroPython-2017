#!/usr/bin/env python

import sys
import pytest
import os.path
from unittest import mock
import unittest
from mailroom.transactions import Transactions
from mailroom.ui import Mailroom


@pytest.fixture
def interactor():
    return Mailroom(Transactions())


@mock.patch('builtins.input')
class TestUI():

    def test_collect_donor_valid(self, mocked_input, interactor):
        mocked_input.side_effect = ["Tommy Vietor", "350"]
        output = interactor.collect_donor_input()
        assert output == ("Tommy Vietor", 350)

    def test_collect_donor_invalid(self, mocked_input, interactor):
        # this seems hacky but I don't have assertRaises() available
        mocked_input.side_effect = ["Tommy Vietor", "pundit the dog"]
        try:
            interactor.collect_donor_input()
        except ValueError:
            assert True
        else:
            assert False

    def test_get_user_input(self, mocked_input, interactor):
        interactor.get_user_input("Some prompt")
        mocked_input.assert_called_once_with("Some prompt")

    def test_error_get_user_input(self, mocked_input, interactor):
        mocked_input.side_effect = TypeError
        output = interactor.get_user_input("Some prompt")
        assert output is None

    def test_collect_challenge_input(self, mocked_input, interactor):
        mocked_input.side_effect = ["3", "100", "400"]
        output = interactor.collect_challenge_input()
        assert output == (3, 100, 400)

    def test_collect_challenge_input_invalid(self, mocked_input, interactor):
        mocked_input.side_effect = ["3", "receipt", "400"]
        output = interactor.collect_challenge_input()
        assert output is None

    def test_safe_input(self, mocked_input, interactor):
        assert interactor.safe_input() is None

    # def test_quit_code(self, mocked_input, interactor):
    # Does not work
    #     with mocked_input.assertRaises(SystemExit):
    #         interactor.quit_code()

    def test_return_to_menu(self, mocked_input, interactor):
        assert interactor.return_to_menu() is True

    # def test_main_loop1(self, mocked_input, interactor):
    # Does not work
    #     stdin = sys.stdin
    #     sys.stdin = open("simulatedinput.txt","r")
    #     interactor.mainloop()
    #     assert interactor.run_interactive_loop.assert_called_once()

    # def test_sending_letters(self, mocked_input, interactor):
    # Does not work
    #     name, amt = ("Ada Lovelace", 345)
    #     name2, amt2, amt3 = ("Marge Simpson", 500, 1000)
    #     t = interactor
    #     t.add_donor(name, amt)
    #     t.add_donor(name2, amt2)
    #     t.add_donor(name2, amt3)
    #     interactor.send_letters()
    #     assert os.path.isfile('Ada_Lovelace.txt')

    def test_update_donors(self, mocked_input, interactor):
        mocked_input.side_effect = ["Tommy", "300"]
        output = interactor.update_donors()
        fs = "your generosity and recent gift"
        assert fs in output

    def test_invalid_update_donors(self, mocked_input, interactor):
        mocked_input.side_effect = ["Tommy", "bad dog"]
        output = interactor.update_donors()
        assert output is None

    def test_challenge_projections(self, mocked_input, interactor):
        mocked_input.side_effect = ["2", "100", "399"]

    def hi(self):
        return "hi"

    def bye(self):
        return "bye"

    def test_select_action(self, mocked_input, interactor):
        argdict = {"1": self.hi, "2": self.bye}
        output = interactor.select_action(argdict, "1")
        assert output == "hi"

    def test_invalid_select_action(self, mocked_input, interactor):
        argdict = {"1": self.hi, "2": self.bye}
        output = interactor.select_action(argdict, "3")
        assert output is False











