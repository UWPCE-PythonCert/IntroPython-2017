#!/user/bin/env python3

import kwargs_ex


def test_yarp():
    assert True


def test_narp():
    result = kwargs_ex.fun(fore_color='blue',
                            back_color='red',
                            link_color='yellow',
                            visited_color='green')
    assert result == ('blue', 'red', 'yellow', 'green')