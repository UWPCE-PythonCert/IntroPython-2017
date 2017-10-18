#!/usr/bin/env python

def exchange_first_last(seq):
    if len(seq) <= 1:
        return seq
    else:
        return(seq[-1:] + seq[1:-1] + seq[:1])





if __name__ == '__main__':

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    print(exchange_first_last(a_string))
    print(exchange_first_last(a_tuple))

    #assert exchange_first_last(a_string) == "ghis is a strint"
    #assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)