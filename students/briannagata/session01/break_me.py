# Python pushups module.
# Python 3.6


def name_error():
    """ Raises exception NameError """
    return name


def type_error():
    """ Raises exception TypeError """
    return ''.join(['', 1])


def syntax_error():
    """ Raises exception SyntaxError """
    return eval('')


def attribute_error():
    """ Raises exception AttributeError """
    return list('attribute').split()
