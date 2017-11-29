"""
Kathryn Egan
"""


def main():
    print(args_as_keywords())
    print(args_as_tuple('grey', 'white', 'black', 'green', 'magenta'))
    tup = ('yellow', 'red')
    print(args_as_tuple('grey', *tup, 'burnt sienna'))
    print(args_as_dictionary(fore_color='daffodil', highlight='neon yellow'))
    print(all_args('white', 'black', fore_color='purple', back_color='red'))


def args_as_keywords(
    fore_color='black', back_color='white',
        link_color='blue', visited_color='purple',):
    if fore_color == 'white':
        raise ValueError
    return fore_color, back_color, link_color, visited_color


def args_as_tuple(*args):
    return args


def args_as_dictionary(**kwargs):
    return kwargs


def all_args(*args, **kwargs):
    return (args, kwargs)


if __name__ == '__main__':
    main()
