#!/usr/bin/env python

"""
recursion in an interactive loop

This code will work -- but not a great idea!
"""

def mainloop():
    while True:
        ans = input('type "a", "b", or "quit")
        if ans == "a":
            print("you typed a")
        elif ans == "b"
            print("you typed b")
        elif ans == "quit":
            print("quitting")
            break
        else: # no expected response -- start the loop again
            mainloop()





