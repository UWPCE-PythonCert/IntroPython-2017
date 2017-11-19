'''test
'''
import kwargs_ex

def test_basic():
    '''test'''
    assert True


#def test_basic_f():
#    assert False

def test_kw():
    '''test'''
    result = kwargs_ex.fun(fore_color='blue',
                            back_color='red',
                            link_color='yellow',
                            visited_color='green')
    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_new_order():
    '''test'''
    result = kwargs_ex.fun(back_color='red',
                            fore_color='blue',
                            link_color='yellow',
                            visited_color='green')
    assert result == ('blue', 'red', 'yellow', 'green')


def test_kw_new_params():
    '''test'''
    result = kwargs_ex.fun('green', 'blue', 'yellow', 'red')
    assert result == ('blue', 'red', 'yellow', 'green')

def test_kw_combo():
    '''test'''
    result = kwargs_ex.fun('blue', 'red', 'yellow', 'red')
    assert result == ('blue', 'red', 'yellow', 'red')
    