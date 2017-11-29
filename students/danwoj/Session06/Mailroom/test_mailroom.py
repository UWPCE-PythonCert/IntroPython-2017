#!/usr/bin/env python3.6

import mailroom

import pytest

def test_add_name():
	assert mailroom.add_name('Dan', 'Woj') is True

def test_add_name2(capsys):
	mailroom.add_name('Dan', 'Woj')
	out, err = capsys.readouterr()
	assert out == 'The name Dan Woj is not in the donor list. Adding them as a new donor.\n\n'

def test_add_value():
	

def test_print_letter():
	assert mailroom.print_letter(4, 1234) is True

def test_run_report(capfd):
	mailroom.run_report()
	out, err = capfd.readouterr()
	assert out == '\n######################  Donor Report ######################\n\nDonor Name         | Total Given | Num Gifts | Average Gift\n-----------------------------------------------------------\nBill Gates         | $ 700.00    | 2         | $ 350.00\nMelvin Smith       | $ 8000.00   | 3         | $ 2666.67\nDaphnie Jones      | $ 2000.00   | 2         | $ 1000.00\nChauncey Doe       | $ 400.00    | 1         | $ 400.00\nFrieda Whatever    | $ 9000.00   | 3         | $ 3000.00\n'