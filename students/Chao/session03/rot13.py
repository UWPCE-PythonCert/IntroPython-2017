#!/usr/bin/env python

# Build a translation table
tran13 = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")

def rot13(x):
    """ Use the table above to encrypt/decrypt """
    return x.translate(tran13)

if __name__ == '__main__':
    """ Some tests """

    # Decrypt the example
    print(rot13("Zntargvp sebz bhgfvqr arne pbeare"))

    # Encrypt Hello World
    print(rot13("Hello World!"))

    assert rot13("Uryyb Jbeyq!") == "Hello World!"
    print("passed!")
