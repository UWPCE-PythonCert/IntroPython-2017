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

@pytest.fixture
def someTransactions():
    t = Transactions()
    name, amt = ("Ada Lovelace", 345)
    name2, amt2, amt3 = ("Marge Simpson", 500, 1000)
    t.add_donor(name, amt)
    t.add_donor(name2, amt2)
    t.add_donor(name2, amt3)
    return Mailroom(t)

class TestPrintsUI():

    @mock.patch('sys.stdout')
    def test_list_donors(self, mockStdout, someTransactions):   
        someTransactions.list_donors()
        result = [call('Donor Names:\nAda Lovelace\nMarge Simpson'), call('\n')]
        mockStdout.write.assert_has_calls([mockStdout.call(result)])




