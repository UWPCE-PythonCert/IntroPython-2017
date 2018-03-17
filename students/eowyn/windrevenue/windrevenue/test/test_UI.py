#!/usr/bin/env python
import sys
import pytest
import os.path
from unittest import mock
import unittest
from windrevenue.UI import UI

# to do: test interactive loops

@mock.patch('builtins.input')
class TestUI():

    def test_get_user_input(self, mocked_input):
        UI().get_user_input("Some prompt")
        mocked_input.assert_called_once_with("Some prompt")

    def test_return_to_menu(self, mocked_input):
        assert UI().return_to_menu() is True

    def hi(self):
        return "hi"

    def bye(self):
        return "bye"

    def test_select_action(self, mocked_input):
        argdict = {"1": self.hi, "2": self.bye}
        output = UI().select_action(argdict, "1")
        assert output == "hi"

    def test_invalid_select_action(self, mocked_input):
        argdict = {"1": self.hi, "2": self.bye}
        output = UI().select_action(argdict, "3")
        assert output is False

