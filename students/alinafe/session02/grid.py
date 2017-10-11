Grid Printer Exercise:

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print ('+ - - - -'),

def print_post():
    print ('|        ',)

def print_beams():
    do_twice(print_beam)
    print ('+')

def print_posts():
    do_twice(print_post)
    print ('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()

\
def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print '+',

def print_dash():
    print '-',

def print_bar():
    print '|',

def print_space():
    print ' ',

def print_end():
    print

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

print_grid()