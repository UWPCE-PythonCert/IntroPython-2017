import unittest.mock as mock
import csv


def please_work(infile_name):
    rate_all = csv.reader(open(infile_name))
    #return ''.join([''.join(x) for x in rate_all])
    return [x for x in rate_all]


def test_thing():
    mock_data = ["1,2,3","4,5,6"]
    with mock.patch('builtins.open', return_value=mock_data) as m:
        print(m)
        print(dir(m))
        result = please_work('foo2')

    m.assert_called_once_with('foo')
    assert result == [["1", "2", "3"], ["4", "5", "6"]]
    #assert False
