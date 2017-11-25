'''Unit Test for mailroom4'''

import json
import mock
import mailroom4 as m4

persistantdata = "mailroomdata_try.json"
maildata = m4.open_json(persistantdata)

def test_open_json():
    '''Opens a JSON file and returns the JSON data as a dictionary.'''
    file = open("mailroomdata.json")
    expected = '{"John Dill": [10.0, 20.0, 30.0], "Sarah Pickle": [10.0, 20.0, 30.0], "Ornett Salt": [10.0, 20.0, 30.0], "Fanny Pepper": [10.0, 20.0, 30.0], "Jo Fang": [50.0]}'
    assert expected==file.read()


def test_write_json():
    '''Write dictionary as JSON to the target filename.'''
    jsondata_dict = {"test":"value"}
    jsondata_test = str(jsondata_dict)
    filename_test = "test.json"
    testout = open(filename_test, "w")
    testout.write(jsondata_test)
    testout.close()
    file = open(filename_test)
    assert jsondata_test == file.read()


def test_make_thanks():
    '''Takes the name and donation and return a thank you text.'''
    assert m4.make_thanks(name="Ed", donation=100) == '''
    Dear Ed,

    Thank you for your generous donation of $ 100. Your
    support enables us to keep doing good in the world. Which means
    your money, earned through whatever means money is earned in
    the amounts you have earned, is now doing good. We thank you. The
    world thanks you.

    Regards,
    Foundation Against Suffering

    '''


def test_send_thank_list():
    with mock.patch('builtins.input',return_value='list'):
        assert m4.send_thank() == "listed"

def test_send_thank_newtolist_exist():
    with mock.patch('builtins.input',return_value="99"):
        assert m4.send_thank(thanks="Test Man", amount=99) == "Add to new."


def test_send_thank_newtolist_new():
    with mock.patch('builtins.input',return_value="99"):
        assert m4.send_thank(thanks="Test Man", amount=99) == "Add to existing."


def test_create_report():
    '''Print the report.'''
    assert m4.create_report() == "Report..."


def test_exitmail():
    '''Save the data; close the app.'''
    file = open("mailroomdata.json")
    expected = '{"John Dill": [10.0, 20.0, 30.0], "Sarah Pickle": [10.0, 20.0, 30.0], "Ornett Salt": [10.0, 20.0, 30.0], "Fanny Pepper": [10.0, 20.0, 30.0], "Jo Fang": [50.0]}'
    assert expected==file.read()


# def test_mainloop():
#     '''Central loop of the app.'''
#     assert m4.mainloop() == ""
