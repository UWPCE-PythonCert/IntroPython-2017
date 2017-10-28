#!/usr/bin/env python

def rot13(a_string):
    ''' Encode any string using rot13 encoding, preserving 
    whitespace, punctuation, and capitalization '''
    import codecs
    return codecs.encode(a_string,encoding="rot13")


if __name__=="__main__":
    assert rot13(rot13("how to cook everything!")) == "how to cook everything!"
    assert rot13(rot13("How to Cook Everything!")) == "How to Cook Everything!"
    assert rot13(rot13("Burr, by Gore Vidal")) == "Burr, by Gore Vidal"
    assert(rot13("Zntargvp sebz bhgfvqr arne pbeare")) == "Magnetic from outside near corner"