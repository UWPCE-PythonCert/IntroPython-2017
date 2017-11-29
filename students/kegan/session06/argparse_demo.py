"""
Kathryn Egan

https://docs.python.org/3/library/argparse.html
"""


def verbose_way():
    """ Verbose, ugly way of dealing with command-line args."""
    import sys

    usage = \
        'USAGE: argparse_demo.py [course] [name] ' +\
        '[grade] [--nickname NICKNAME] [--honors]'
    my_args = {
        'course': '',
        'name': '',
        'grade': '',
        'nickname': '',
        'honors': False}
    positionals = ['course', 'name', 'grade']
    skip_next = False

    # iteratively evaluate command-line arguments
    for index, item in enumerate(sys.argv[1:]):
        if skip_next:
            skip_next = False
        # flag indicating next argument is nickname
        elif item in ('--nickname', '-n'):
            try:
                my_args['nickname'] = sys.argv[index + 2]
            except IndexError:
                print(usage)
                sys.exit()
            else:
                skip_next = True
        # flag indicating honors class
        elif item in ('--honors', '-H'):
            my_args['honors'] = True
        # positional argument
        else:
            try:
                my_args[positionals[0]] = item
            except IndexError:
                print(usage)
                print(my_args)
                sys.exit()
            positionals = positionals[1:]

    # make sure all positional arguments have been specified
    if len(positionals) != 0:
        print(usage)
        sys.exit()

    # make sure grade is a float
    try:
        my_args['grade'] = float(my_args['grade'])
    except ValueError:
        print("grade must be a float")
        sys.exit()

    # print output
    nickname = ', aka {},'.format(
        my_args['nickname']) if my_args['nickname'] else ''
    honors = ' (Honors)' if my_args['honors'] else ''
    print(
        "{}{} received a {:.1f} in {}{}.".format(
            my_args['name'].title(), nickname, my_args['grade'],
            my_args['course'], honors))


def argparse_way():
    """ Simple, descriptive way of dealing with command-line args. """
    from argparse import ArgumentParser

    parser = ArgumentParser()
    # add a positional argument
    parser.add_argument('course')
    # include a help message
    parser.add_argument('name', help='name of student')
    # specify the type
    parser.add_argument('grade', help='student grade', type=float)
    # add an optional argument
    parser.add_argument('--nickname', '-n', help='student nickname (optional)')
    # add a flag
    parser.add_argument(
        '--honors', '-H', action='store_true',
        help='honors class (optional)')
    # parse command-line arguments
    args = parser.parse_args()

    # print output
    nickname = ', aka {},'.format(args.nickname) if args.nickname else ''
    honors = ' (Honors)' if args.honors else ''
    print(
        "{}{} received a {:.1f} in {}{}.".format(
            args.name, nickname, args.grade, args.course, honors))

# docopt
# click


if __name__ == '__main__':
    # verbose_way()
    argparse_way()
