#! /usr/bin/env python


def decimal_to_hex_dict_string_comp():
    """ Use a list comprehension to make a dictionary that maps
        decimal, 0 - 15, to hex.
    """
    dec_list = [str(dec) for dec in range(0, 16)]
    dec_hex_dict = {digit: hex(int(digit)) for digit in dec_list}
    return dec_hex_dict


def decimal_to_hex_dict_dict_comp():
    dec_hex_dict = {dec: hex(dec) for dec in range(0, 16)}
    return dec_hex_dict


if __name__ == "__main__":

    print(decimal_to_hex_dict_string_comp())
    print(decimal_to_hex_dict_dict_comp())
