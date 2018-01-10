#!/usr/bin/python



def safe_input(f):
    try:
        f = input('input something please!')
    except KeyboardInterrupt:
        raise
        print('Please do not attempt to quit my program.....')
    return f

