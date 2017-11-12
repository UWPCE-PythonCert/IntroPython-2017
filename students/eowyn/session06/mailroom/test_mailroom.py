#!/usr/bin/env python

import mailroom
import os.path


def test_safeinput():
    result = mailroom.safe_input()
    assert result is None


def test_return_to_menu():
    result = mailroom.return_to_menu()
    assert result is True


def test_generate_letter():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    returnval = mailroom.generate_letter('Margaret Atwood')
    assert "Margaret Atwood" in returnval
    assert "$555" in returnval


def test_generate_report_data():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    returnval = set(mailroom.generate_report_data())
    assert len(mailroom.DONORS) == len(returnval)
    assert ('Fred Armisen', 1662, 3, 554) in returnval


def test_setup_table():
    returnval = mailroom.setup_table()
    assert returnval.startswith("Donor Name")
    assert "Total Given" in returnval
    assert "Num Gifts" in returnval
    assert "Average Gift" in returnval


def test_setup_body():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    list_data = mailroom.generate_report_data()
    returnval = mailroom.setup_body(list_data)
    nlines = returnval.count('\n')
    assert "Margaret Atwood" in returnval
    assert "Fred Armisen" in returnval
    assert nlines == len(mailroom.DONORS)


def test_remove_inputquotes():
    output = 'hello'
    assert mailroom.remove_inputquotes("hello") == output


def test_retrieve_donor_exists():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    name = "Margaret Atwood"
    output = [300, 555]
    assert mailroom.retrieve_donations(name) == output


def test_retrieve_donations_new():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    assert mailroom.retrieve_donations("Paul Simon") is None


def test_add_donation_new():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    name = "Bob Mueller"
    amount = 500
    mailroom.add_donation(name, amount)
    assert mailroom.retrieve_donations(name) == [amount]


def test_add_donation_existing():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    name = "Fred Armisen"
    amount = 500
    mailroom.add_donation(name, amount)
    assert mailroom.retrieve_donations(name)[-1] == amount


def test_file_existance():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    mailroom.send_letters()
    assert os.path.isfile("Margaret_Atwood.txt")
    assert os.path.isfile("Fred_Armisen.txt")
    assert os.path.isfile("Heinz_the_Baron_Krauss_von_Espy.txt")


def test_select_action_bad():
    arg_dict = {"1": mailroom.update_donors,
                "2": mailroom.send_letters}
    assert mailroom.select_action(arg_dict, "5") is False


def test_donor_list():
    mailroom.DONORS = {'Fred Armisen': [240, 422, 1000],
                       'Heinz the Baron Krauss von Espy': [1500, 2300],
                       'Margaret Atwood': [300, 555]}
    returnval = mailroom.make_donor_list()
    nlines = returnval.count('\n')
    assert returnval.startswith("Donor Names:")
    assert "Margaret Atwood" in returnval
    assert "Fred Armisen" in returnval
    assert nlines == len(mailroom.DONORS)


def test_elect_action_good():
    arg_dict = {"1": some_function, "2": mailroom.send_letters}
    x = mailroom.select_action(arg_dict, "1")
    assert x == 'this worked'


def some_function():
    return "this worked"
