#!/usr/bin/env python

# hello_name

def hello_name(name):
    return 'Hello ' + name + '!'

assert hello_name('Bob') == 'Hello Bob!'
assert hello_name('Alice') == 'Hello Alice!'
assert hello_name('X') == 'Hello X!'

# make_abba

def make_abba(a, b):
    return a + b*2 + a

assert make_abba('Hi', 'Bye') == 'HiByeByeHi'
assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
assert make_abba('What', 'Up') == 'WhatUpUpWhat'


# make_tags

def make_tags(tag, word):
    op = '<' + tag + '>'
    cl = '</' + tag + '>'
    return op + word + cl

assert make_tags('i', 'Yay') == '<i>Yay</i>'
assert make_tags('i', 'Hello') == '<i>Hello</i>'
assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'


# make_out_word

def make_out_word(out, word):
    op = out[0:2]
    cl = out[2:]
    return op + word + cl

assert make_out_word('<<>>', 'Yay') == '<<Yay>>'
assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'
assert make_out_word('[[]]', 'word') == '[[word]]'

# extra_end

def extra_end(str):
    return str[-2:]*3

assert extra_end('Hello') == 'lololo'
assert extra_end('ab') == 'ababab'
assert extra_end('Hi') == 'HiHiHi'

# first_two

def first_two(str):
    if len(str) < 2:
    	return str
    else:
    	return str[0:2]
assert first_two('Hello') == 'He'
assert first_two('abcdefg') == 'ab'
assert first_two('ab') == 'ab'


# first_half

def first_half(str):
    if (len(str) % 2) == 0:
    	return str[0:(len(str)//2)]

assert first_half('WooHoo') == 'Woo'
assert first_half('HelloThere') == 'Hello'
assert first_half('abcdef') == 'abc'


# without_end

def without_end(str):
    return str[1:-1]

assert without_end('Hello') == 'ell'
assert without_end('java') == 'av'
assert without_end('coding') == 'odin'

# combo_string

def combo_string(a, b):
    if len(a) < len(b):
    	return a+b+a
    else: 
    	return b+a+b


assert combo_string('Hello', 'hi') == 'hiHellohi'
assert combo_string('hi', 'Hello') == 'hiHellohi'
assert combo_string('aaa', 'b') == 'baaab'

# non_start

def non_start(a, b):
    return a[1:] + b[1:]
assert non_start('Hello', 'There') == 'ellohere'
assert non_start('java', 'code') == 'avaode'
assert non_start('shotl', 'java') == 'hotlava'


#left2

def left2(str):
    return str[2:] + str[0:2]
assert left2('Hello') == 'lloHe'
assert left2('java') == 'vaja'
assert left2('Hi') == 'Hi'
