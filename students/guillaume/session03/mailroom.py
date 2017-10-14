#!/usr/bin/env python3
def read_data(textfile):
    '''
    '''
    file = open(textfile, 'r')
    donors = list()
    for i in list(file.readlines()):
        donors.append((i.rstrip()).split(','))
        for i, s in enumerate(donors[-1]):
            donors[-1][i] = s.lstrip()
            if donors[-1][i].isdecimal():
                print(s)
                donors[-1][i] = float(s)
    file.close()
    return donors


def input_sc():
    '''
    '''
    welcome = """
            local charity donor database\n

                Please make a choice:

                  1 - Send a thank you
                  2 - Create a report
                  3 - Quit\n
                """
    print(welcome)
    bool = True
    while bool:
        selection = input('Please type a number between 1 & 3:\n')
        if selection.isdecimal():
            selection = int(selection)
            if selection > 0 and selection < 4:
                bool = False


if __name__ == '__main__':
    '''
    '''
    print(read_data('donors.txt'))
    input_sc()
