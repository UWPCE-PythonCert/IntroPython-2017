#!/usr/bin/env python

import pytest
from unittest import mock
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
        mocked_input.side_effect = ["Tommy Vietor", "pundit the dog"]
        output = interactor.collect_donor_input()
        assert output is None


    def test_get_user_input(self, mocked_input, interactor):
        output = interactor.get_user_input("Some prompt")
        mocked_input.assert_called_once_with("Some prompt")

    def test_error_get_user_input(self, mocked_input, interactor):
        mocked_input.side_effect = TypeError
        output = interactor.get_user_input("Some prompt")
        assert output is None

    def test_collect_challenge_input(self, mocked_input, interactor):
        mocked_input.side_effect = ["3", "100", "400"]
        output = interactor.collect_challenge_input()
        assert output == (3, 100, 400)


    def test_collect_challenge_input(self, mocked_input, interactor):
        mocked_input.side_effect = ["3", "receipt", "400"]
        output = interactor.collect_challenge_input()
        assert output is None





