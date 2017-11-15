"""
Kathryn Egan
"""
import pytest
import kwargs_lab


def test_pass():
    assert True


# def test_fail():
#     a = 5
#     b = 6
#     assert a == b


def test_keyword_args():
    result = kwargs_lab.args_as_keywords(
        fore_color='blue', back_color='red',
        link_color='yellow', visited_color='green')
    assert result == ('blue', 'red', 'yellow', 'green')
    assert (
        kwargs_lab.args_as_keywords('red', 'blue', 'yellow', 'chartreuse') ==
        ('red', 'blue', 'yellow', 'chartreuse'))
    assert (
        kwargs_lab.args_as_keywords(link_color='red', back_color='blue') ==
        ('black', 'blue', 'red', 'purple'))
    assert (
        kwargs_lab.args_as_keywords(
            'purple', link_color='red', back_color='blue') ==
        ('purple', 'blue', 'red', 'purple'))
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert (
        kwargs_lab.args_as_keywords(*regular, **links) ==
        ('red', 'blue', 'chartreuse', 'purple'))
    with pytest.raises(ValueError):
        kwargs_lab.args_as_keywords(fore_color='white')


def test_tuple_args():
    assert (
        kwargs_lab.args_as_tuple('blue', 'green', 'purple') ==
        ('blue', 'green', 'purple'))


def test_dictionary_args():
    assert (
        kwargs_lab.args_as_dictionary(link_color='red', back_color='yellow') ==
        {'link_color': 'red', 'back_color': 'yellow'})


def test_all_args():
    assert (
        kwargs_lab.all_args('red', 'yellow', key1='value1', key2='value2') ==
        (('red', 'yellow'), {'key1': 'value1', 'key2': 'value2'}))
