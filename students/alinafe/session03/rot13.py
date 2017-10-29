#!/usr/bin/env python3
"""
The task
Add a python module named rot13.py to the session03 dir in your student dir.
This module should provide at least one function called rot13 that takes any
amount of text and returns that same text encrypted by ROT13.

This function should preserve whitespace, punctuation and capitalization.

Your module should include an if __name__ == '__main__': block with tests (asserts)
 that demonstrate that your rot13 function and any helper functions you add work properly.

ordinals…
“Ordinals” are the numerical values associated with characters. Python stringsl are native unicode,
so the number values of any character

Hints
Note that the alphabet has 26 letters, so if you “rotate” by 13 letters twice, you will be back were you started.
So if you call your function twice on a string, you should get the same string back.

rot13(rot13(something)) == something

There is a “short-cut” available that will help you accomplish this task. Some spelunking
in the documentation for strings should help you to find it. If you do find it, using it is completely fair game.

As usual, add your new file to your local clone right away. Make commits early and often
and include commit messages that are descriptive and concise.

When you are done, if you want me to review it, push your changes to github and issue a pull request.

Try decrypting this:

“Zntargvp sebz bhgfvqr arne pbeare”

"""

#ord('A') = 65
#ord('Z') = 90
#ord('a') = 97
#ord('z') = 122


def setn(x, low, high):
    while x > high:
        x -= 26
    while x < low:
        x += 26
    return x
#set the high and low
#>>> set(2, 65,90)
#80
#>>> chr(80)
#'P'
#>>> setnorm(90, 65,90)
#90
#>>> chr(90)
#'Z'

def rot13(word, num):
    some_word = ''
    for l in word:
        if l.isupper():
            some_word += chr(setn(ord(l) + num, 65, 90))

            #https://docs.python.org/3/library/functions.html#ord
            #For example, ord('A) returns the integer 65
        elif not l.isalpha():
            some_word += l
        else:
            some_word += chr(setn(ord(l) + num, 97, 122))
            #https://docs.python.org/3/library/functions.html#chr
            #For example, chr(97) and chr(122) returns the string 'a' and 'z' respectively
    return some_word

print(rot13("Zntargvp sebz bhgfvqr arne pbeare", 13))
#(if Z=90)+13 = 77 = M etc..
#Magnetic from outside near corner


if __name__ == "__main__":
    print (rot13("Zntargvp sebz bhgfvqr arne pbeare",13))


    assert (rot13("Zntargvp sebz bhgfvqr arne pbeare",13) ==
            "Magnetic from outside near corner")
