"""
Kathryn Egan

Prompts user for a string that it will encode according
to ROT13 protocol and print to console.
"""


def main():
    """ Main module for encoding strings."""
    test_string = 'This IS A    TEST. %92??'
    assert encode(encode(test_string)) == test_string

    while True:
        in_string = input('Enter string to encode/decode (Q to quit)\n>')
        if in_string.upper() == 'Q':
            break
        print(encode(in_string))


def encode(in_string):
    """ Encodes given string per ROT13 protocol.
    Preserves numbers, whitespace, punctuation, capitalization.
    Args:
        in_string (str) : string to encode
    Returns:
        str : encoded string
    """
    out_string = []
    for char in in_string:
        if char.isalpha():
            numeric = ord(char) + 13
            if numeric > max_value(char):
                numeric -= 26
        out_string.append(char)
    return out_string


def max_value(char):
    """ Returns max allowed numeric value
    depending on whether the char is upper or lower.
    Args:
        char (str) : character to evaluate
    Returns:
        int : 90 if char is upper, otherwise 122
    """
    return 90 if char.isupper() else 122


if __name__ == '__main__':
    main()
