"""
author@kathrynegan

Causes and catches NameError, AttributeError,
and TypeError in code and prints message if
error was successfully generated.
SyntaxError code included and commented out.
"""


def cause_name_error():
    try:
        print(name)
    except NameError:
        print('Successful NameError')
        return
    print('No NameError')


def cause_type_error():
    try:
        string = 'string'
        string += 1
    except TypeError:
        print('Successful TypeError')
        return
    print('No TypeError')


def cause_attribute_error():
    class ErrorProne:
        def __init__(self):
            self.value1 = 1
    try:
        error = ErrorProne()
        print(error.value2)
    except AttributeError:
        print('Successful AttributeError')
        return
    print('No AttributeError')


cause_name_error()
cause_type_error()
cause_attribute_error()

# cause syntax error
# while True
#     print('broken')
