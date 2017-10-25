
def exchange_first_last(x):
    return x[-1:]+x[1:-1]+x[:1]

def del_alt(x):
    return x[::2]

def mid_sans_4(x):
    return x[4:-4]


def reverse_slice(x):
    return x[::-1]

def thirds_swap(x):
    y = (int(len(x)/3))
    return x[y:-y] + x[-y:] + x[0:y]
    # [0:y]
    # [y+1:-(y+1)]
    # [-y:]


if __name__ == "__main__": 

    
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == 'ghis is a strint'
    assert exchange_first_last(a_tuple) == (32,54,13,12,5,2)
    assert del_alt(a_string)  == 'ti sasrn'
    assert del_alt(a_tuple) == (2,13,5)
    assert mid_sans_4(a_string) ==  ' is a st'
    assert mid_sans_4(a_tuple) == ()
    assert reverse_slice(a_string) == 'gnirts a si siht'
    assert reverse_slice(a_tuple) == (32,5,12,13,54,2)
    assert thirds_swap(a_string) == 'is a stringthis '
    assert thirds_swap(a_tuple) == (13,12,5,32,2,54)

