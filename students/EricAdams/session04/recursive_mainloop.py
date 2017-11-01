#!/usr/bin/env python

"""
recursion in an interactive loop

This code will work -- but not a great idea!
"""

import sys


def mainloop():
    while True:
        ans = input('type "a", "b", or "quit"')
        if ans == "a":
            print("you typed a")
        elif ans == "b":
            second_loop()
        elif ans[0] == "q":
            print("quitting")
            break
            #sys.exit()  # what if I use the break, rather than the exit()?
        elif ans[0] == "r":  # here to test recursion...
            raise Exception()
        # else:  # no expected response -- start the loop again
        #     mainloop()

def second_loop():
    while True:
        ans = input('type "a", "b", or "go back')
        if ans == "a":
            print("you typed a")
        elif ans == "b":
            second_loop()
        elif ans[0] == "g":
            return



if __name__ == "__main__":
    mainloop()





