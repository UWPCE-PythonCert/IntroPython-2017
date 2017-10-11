#!/usr/bin/python

def raise_name_error():
    print(i_do_no_exist)


def raise_type_error():
    x = 1 + a


def raise_syntax_error():
    eval('x===x')


def raise_attribute_error():
    from time import fakemodule


if __name__ == "__main__":
    try:
        raise_name_error()
    except Exception as e:
        print("#### Name Error ####")
        print(str(e) + "\n")

    try:
        raise_type_error()
    except Exception as e:
        print("#### Type Error ####")
        print(str(e) + "\n")

    try:
        raise_syntax_error()
    except Exception as e:
        print("#### Syntax Error ####")
        print(str(e) + "\n")


    try:
        raise_attribute_error()
    except Exception as e:
        print("#### Attribute Error ####")
        print(str(e) + "\n")
