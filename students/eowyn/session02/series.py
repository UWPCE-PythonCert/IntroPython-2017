#!/usr/bin/env python
"""Return fibbonaci,lucas, and generic summed series series"""

def fib(n):
    """ Print the nth element of the fibbonaci sequence"""
    return sum_series(n)

def lucas(n):
    """ Print the nth element of the lucas sequence"""
    return sum_series(n,2,1)

def sum_series(n,n0=0,n1=1):
    """ Print the nth element of the sum series sequence
        that begins with the elements n0 and n1"""
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-2,n0,n1)+sum_series(n-1,n0,n1)

if __name__=="__main__":
    print("testing fibnnoci sequence")
    assert fib(0)==0
    assert fib(1)==1
    assert fib(2)==1
    assert fib(3)==2
    assert fib(7)==13
    print("testing lucas sequence")
    assert lucas(0)==2
    assert lucas(1)==1
    assert lucas(5)==11
    assert lucas(7)==29
    print("testing generic sequence")
    assert sum_series(0)==0
    assert sum_series(5,2,1)==11
    assert sum_series(3,0,1)==2