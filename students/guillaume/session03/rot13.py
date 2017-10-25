#!/usr/bin/env python3
from string import ascii_lowercase, ascii_uppercase


def rot(n):
    '''
    Generate subsitution cypher table of value n
    Outcome is a tuple with the std alphabet and the rotated one
    '''
    ascii_chars = [ascii_lowercase, ascii_uppercase]
    rot_chars = [alphabet[n:] + alphabet[:n] for alphabet in ascii_chars]

    return ''.join(ascii_chars), ''.join(rot_chars)


def translation(string, n, boolean=True):
    '''
    Provide:
    - translation from natural to encoded by default
    - translation from encoded to natural when boolean == False
    '''
    from_t, to_t = rot(n)
    if not boolean:
        from_t, to_t = to_t, from_t
    trans_table = str.maketrans(from_t, to_t)
    return string.translate(trans_table)


def rot13(string):
    '''
    Provide translation from natural to encoded
    '''
    return translation(string, 13)


def rot13_reverse(string):
    '''
    Provide translation from encoded to natural
    '''
    return translation(string, 13, False)


def sign(integer):
    if integer != 0:
        return integer // abs(integer)
    return 1


def translation_2(string, n):
    '''
    '''
    mid_l = (ord('z') - ord('a') - 1) // 2 + ord('a')
    mid_u = (ord('Z') - ord('A') - 1) // 2 + ord('A')
    new_string = ''
    for char in string:
        if char.isalpha():
            mid = mid_l
            if char.isupper():
                mid = mid_u
            ascii_c = ord(char) + sign(mid - ord(char)) * n
            new_char = chr(ascii_c)
            new_string += new_char
        else:
            new_string += char
    return new_string


def rot13_2ver(string):
    n = 13
    return translation_2(string, n)


if __name__ == '__main__':
    '''
    print(rot(13))
    print(type(rot(13)))
    print(rot13('testo'))
    '''

    print(rot13('abcd wtYuZQc'))
    print(rot13_2ver('abcd wtYuZQc'))

    test_str = 'Zntargvp sebz bhgfvqr arne pbeare'
    print(test_str)
    print(rot13_reverse(test_str))
    print(rot13_2ver(test_str))

    test_str = 'Magnetic from outside near corner'
    print(test_str)
    assert print(rot13_reverse(test_str)) == print(rot13_2ver(test_str))
    

    test_str = 'Zz Aa Nn'
    print(test_str)
    print(rot13_reverse(test_str))
    print(rot13_2ver(test_str))
