#!/usr/bin/env python3

def safe_input():
    try:
        x = input("Please enter some text> ")
        return x
    except (EOFError, KeyboardInterrupt) as e:
        return None


if __name__ == "__main__":
    print(safe_input())
