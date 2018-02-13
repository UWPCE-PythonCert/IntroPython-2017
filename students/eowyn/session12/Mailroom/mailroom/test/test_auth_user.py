#!/usr/bin/env python

import pytest
from unittest import mock
from mailroom.authorized_users import UserLogger


@pytest.fixture
def decorated_function():
    ul = UserLogger()

    @ul.record_user
    def some_funct():
        pass
    return some_funct, ul


@mock.patch('builtins.input')
class TestAuthUser():



    def test_auth_user_decorator(self, mocked_input, decorated_function):
        decorated_function[0]()
        mocked_input.assert_called_once()

    def test_auth_user_called_with(self, mocked_input, decorated_function):
        decorated_function[0]()
        mocked_input.assert_called_once_with("Please enter user name:\n")


    def test_auth_user(self, mocked_input, decorated_function):
        assert decorated_function[1].users == []
        mocked_input.return_value = 'Rod Rosenstein'
        decorated_function[0]()
        assert decorated_function[1].users == ['Rod Rosenstein']